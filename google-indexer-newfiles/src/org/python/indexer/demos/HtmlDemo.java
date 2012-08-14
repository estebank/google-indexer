/**
 * Copyright 2009, Google Inc.  All rights reserved.
 */
package org.python.indexer.demos;

import org.python.indexer.Indexer;
import org.python.indexer.NBinding;
import org.python.indexer.StyleRun;
import org.python.indexer.Util;

import java.io.File;
import java.util.List;

/**
 * Simple proof-of-concept demo app for the indexer.  Generates a static-html
 * cross-referenced view of the code in a file or directory, using the index to
 * create links and outlines.  <p>
 *
 * The demo not attempt to show general cross references (declarations and uses
 * of a symbol) from the index, nor does it display the inferred type
 * information or generated error/warning diagnostics.  It could be made to do
 * these things, as well as be made more configurable and generally useful, with
 * additional effort.<p>
 *
 * Run it from jython source tree root dir with, e.g.: to index <code>/usr/lib/python2.4/email</code>
 * <pre>
 * ant jar &amp; &amp; java -classpath ./dist/jython-dev.jar:./extlibs/antlr-runtime-3.1.3.jar:./extlibs/constantine.jar org.python.indexer.demos.HtmlDemo /usr/lib/python2.4/email
 * </pre>
 *
 * Fully indexing the Python standard library may require a more complete build to pick up all the dependencies:
 * <pre>
 * rm -rf ./html/ &amp;&amp; ant clean &amp;&amp; ant jar &amp;&amp; ant jar-complete &amp;&amp; java -classpath ./dist/jython.jar:./extlibs/antlr-runtime-3.1.3.jar:./extlibs/constantine.jar org.python.indexer.demos.HtmlDemo /usr/lib/python2.4/
 * </pre>
 */
public class HtmlDemo {

    private static final File OUTPUT_DIR =
            new File(new File("./html").getAbsolutePath());

    private static final String CSS =
            ".builtin {color: #5b4eaf;}\n" +
            ".comment, .block-comment {color: #005000; font-style: italic;}\n" +
            ".constant {color: #888888;}\n" +
            ".decorator {color: #778899;}\n" +
            ".doc-string {color: #005000;}\n" +
            ".error {border-bottom: 1px solid red;}\n" +
            ".field-name {color: #2e8b57;}\n" +
            ".function {color: #880000;}\n" +
            ".identifier {color: #8b7765;}\n" +
            ".info {border-bottom: 1px dotted RoyalBlue;}\n" +
            ".keyword {color: #0000cd;}\n" +
            ".lineno {color: #aaaaaa;}\n" +
            ".number {color: #483d8b;}\n" +
            ".parameter {color: #2e8b57;}\n" +
            ".string {color: #4169e1;}\n" +
            ".type-name {color: #4682b4;}\n" +
            ".warning {border-bottom: 1px dotted orange;}\n";

    private Indexer indexer;
    private File rootDir;
    private Linker linker;

    private static void abort(String msg) {
        System.err.println(msg);
        System.exit(1);
    }

    private void info(Object msg) {
        System.out.println(msg);
    }

    private void makeOutputDir() throws Exception {
        if (!OUTPUT_DIR.exists()) {
            OUTPUT_DIR.mkdirs();
            info("created directory: " + OUTPUT_DIR.getAbsolutePath());
        }
    }

    private void generateHtml() throws Exception {
        info("generating html...");
        makeOutputDir();
        Util.writeFile(cssPath(), CSS);
        linker = new Linker(rootDir, OUTPUT_DIR);
        linker.findLinks(indexer);

        int rootLength = (int)rootDir.getAbsolutePath().length();
        for (String path : indexer.getLoadedFiles()) {
            if (!path.startsWith(rootDir.getAbsolutePath())) {
                continue;
            }
            File destFile = Util.joinPath(OUTPUT_DIR, path.substring(rootLength));
            destFile.getParentFile().mkdirs();
            String destPath = destFile.getAbsolutePath() + ".html";
            String html = markup(path);
            Util.writeFile(destPath, html);
        }

        info("wrote " + indexer.getLoadedFiles().size() + " files to " + OUTPUT_DIR);
    }

    private String markup(String path) throws Exception {
        String source = Util.readFile(path);

        List<StyleRun> styles = new Styler(indexer, linker).addStyles(path, source);
        styles.addAll(linker.getStyles(path));

        source = new StyleApplier(path, source, styles).apply();

        String outline = new HtmlOutline(indexer).generate(path);

        return "<html><head title=\"" + path + "\">"
                + "<link rel=StyleSheet href=\"" + cssPath()
                + "\" type=\"text/css\" media=\"screen\">"
                + "</head>"
                + "<body>"
                + "<table width=100% border='1px solid gray'><tr><td valign='top'>"
                + outline
                + "</td><td>"
                + "<pre>" + addLineNumbers(source) + "</pre>"
                + "</td></tr></table></body></html>";
    }

    private String cssPath() {
        return Util.joinPath(OUTPUT_DIR.getAbsolutePath(), "demo.css").toString();
    }

    private String addLineNumbers(String source) {
        StringBuilder result = new StringBuilder((int)(source.length() * 1.2));
        int count = 1;
        for (String line : source.split("\n")) {
            result.append("<span class='lineno'>");
            result.append(count++);
            result.append("</span> ");
            result.append(line);
            result.append("\n");
        }
        return result.toString();
    }

    private void start(File fileOrDir) throws Exception {
        rootDir = fileOrDir.isFile() ? fileOrDir.getParentFile() : fileOrDir;

        indexer = new Indexer();
        indexer.addPath("/usr/lib/python2.4");
        info("building index...");
        indexer.loadFileRecursive(fileOrDir.getAbsolutePath());
        indexer.ready();

        info(indexer.getStatusReport());
        generateHtml();
    }

    public static void main(String[] args) throws Exception {
        // For now, just parse a file.
        if (args.length < 1) {
            abort("Usage:  java org.python.indexer.HtmlDemo <file-or-directory>");
        }

        File fileOrDir = new File(args[0]);
        if (!fileOrDir.exists()) {
            abort("File not found: " + fileOrDir);
        }

        new HtmlDemo().start(fileOrDir);
    }

}

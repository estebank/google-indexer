/**
 * Copyright 2009, Google Inc.  All rights reserved.
 */
package org.python.indexer;

/**
 * Signals that indexing is being aborted.
 * @see {Indexer#enableAggressiveAssertions}
 */
public class IndexingException extends RuntimeException {

    public IndexingException() {
    }

    public IndexingException(String msg) {
        super(msg);
    }

    public IndexingException(String msg, Throwable cause) {
        super(msg, cause);
    }

    public IndexingException(Throwable cause) {
        super(cause);
    }
}

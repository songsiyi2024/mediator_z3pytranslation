package org.fmgroup.mediator.transforms;

import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.system.System;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.plugins.scheduler.Scheduler;

/**
 * Thin wrapper that reuses the existing Scheduler implementation to flatten a System into
 * a single Automaton. The project already contains a `Scheduler` with `Schedule(System)`
 * that implements the scheduling/flattening (including the external transition scheduling
 * algorithm). Delegate to that implementation for correctness and reuse.
 */
public class SystemFlattener {

    public static Automaton flatten(System sys) throws ValidationException {
        if (sys == null) throw new IllegalArgumentException("System is null");
        // Delegate to Scheduler.Schedule which implements Algorithm 1/2
        return Scheduler.Schedule(sys);
    }
}

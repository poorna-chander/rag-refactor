/**
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id java/example/hello-world
 */

import java

from Call call, Callable callee
where callee.fromSource() and (call.getCallee() = callee) 
        and not call.getFile().getStem().matches("%Tests") 
            and  not callee.getFile().getStem().matches("%Tests")
select call, call.getLocation(), call.getPrimaryQlClasses(), call.getEnclosingCallable(), call.getEnclosingCallable().getLocation(), call.getEnclosingCallable().getPrimaryQlClasses(), call.getFile(),  callee, callee.getLocation(), callee.getFile(), callee.getPrimaryQlClasses()

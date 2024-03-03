/**
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id java/example/hello-world
 */

import java

// ################################################################
//                             CALLER CALLEE pairs details 

// V2
// from Call call, Callable callee
// where callee.fromSource() and (call.getCallee() = callee) 
//         and not call.getFile().getStem().matches("%Tests") 
//             and  not callee.getFile().getStem().matches("%Tests")
// select call, call.getLocation(), call.getEnclosingCallable(), call.getFile(),  call.getPrimaryQlClasses(), callee, callee.getLocation(), callee.getFile(), callee.getPrimaryQlClasses()

// V2
// from Call call, Callable callee
// where callee.fromSource() and (call.getCallee() = callee) 
//         and not call.getFile().getStem().matches("%Tests") 
//             and  not callee.getFile().getStem().matches("%Tests")
// select call, call.getEnclosingCallable(), callee


// V3
from Call call, Callable callee
where callee.fromSource() and (call.getCallee() = callee) 
        and not call.getFile().getStem().matches("%Tests") 
            and  not callee.getFile().getStem().matches("%Tests")
select call, call.getLocation(), call.getPrimaryQlClasses(), call.getEnclosingCallable(), call.getEnclosingCallable().getLocation(), call.getEnclosingCallable().getPrimaryQlClasses(), call.getFile(),  callee, callee.getLocation(), callee.getFile(), callee.getPrimaryQlClasses()


// ###########################################################

//                          DETAILS OF EACH METHOD  

//v1 -- redundant - dont use
// from Class c, Package p
// where c.fromSource() and p.contains(c) and not c.getName().matches("%Tests") 
// select p, c, c.getAMethod(), c.getAMethod().getAParamType().getName(), c.getAMethod().getReturnType().getName()

//v2 -- no param types
// from Package p, Class c, Method m
// where m.fromSource() and p.contains(c) and c.contains(m) and not c.getName().matches("%Tests") 
// select p, m.getFile(), m, m.getReturnType(), m.getLocation() 

//v3 -- PARAMS AS STRING  (no classes only methods)
// from Package p, Class c, Method m
// where m.fromSource() and p.contains(c) and c.contains(m) and not c.getName().matches("%Tests") 
// select p, m.getFile(), m, m.paramsString(), m.getReturnType(), m.getLocation() 

//v4 -- only methods of non void params
// from Package p, Class c, Method m
// where m.fromSource() and p.contains(c) and c.contains(m) and not c.getName().matches("%Tests") 
// select p, m.getFile(), m, m.getAParamType(), m.getReturnType(), m.getLocation() 


//v5 -- PARAMS AS STRING  (classes and methods)
// from Package p, Class c, Callable m
// where m.fromSource() and p.contains(c) and c.contains(m) and not c.getName().matches("%Tests") 
// select p, m.getFile(), m, m.paramsString(), m.getReturnType(), m.getLocation() 



// ###################################################################

// from  Callable callee, Package p
// where callee.fromSource() and not callee.getFile().getStem().matches("%Tests") and p.contains(callee)
// select p, callee.getFile(), callee, callee.getAp(), callee.getReturnType(), callee.getLocation()

// from Method m
// where m.fromSource()
// select m

// from MethodAccess m
// where m.getNumArgument() > 0
// select m



/**
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id java/example/hello-world
 */

import java

from Package p, Class c, Callable m
where m.fromSource() and p.contains(c) and c.contains(m) and not c.getName().matches("%Tests") 
select p, m.getFile(), m, m.paramsString(), m.getReturnType(), m.getLocation() 
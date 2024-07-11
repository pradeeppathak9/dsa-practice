
"""
We want to implement a middleware router for our web service, which based on the path returns different strings (these would represent “functions to invoke” in a real application).
Our interface for the router looks something like:

interface Router {

  fun addRoute(path: String, result: String) : Unit;

  fun callRoute(path: String) : String;

}

Usage:

Router.addRoute("/bar", "result")

Router.callRoute("/bar/dqwd") -> "result"

Router.addRoute("/bar/*/baz", "result bar_baz")

Router.addRoute("/bar/foo/abc", "result foo")
"""


class Router: 
    def __init__(self):
        self.path_mapping = {} 
        
    def addRoute(self, path, result):
        node = self.path_mapping
        for pattern in path.split('/'):
            if pattern not in node:
                node[pattern] = {}
            node = node[pattern]            
        node['result'] = result


    def callRoute(self, path):
        result = None
        def dfs(node, path):
            if len(path) == 0:
                nonlocal result
                if result is not None: 
                    return
                if 'result' in node: 
                    result = node['result']
            else:
                if path[0] in node:
                    dfs(node[path[0]], path[1:])
                if '*' in node: 
                    dfs(node['*'], path[1:])
        
        dfs(self.path_mapping, path.split('/'))
        if result:
            return result
        raise Exception(f"Requested Path '{path}' doesn't exist")


if __name__ == '__main__':
    router = Router()
    router.addRoute("/bar", "bar")
    router.addRoute("/bar/foo", "bar/foo")
    router.addRoute("/foo", "Hello foo")
    router.addRoute("/bar/foo/baz", "/bar/foo/baz")
    router.addRoute("/bar/*/baz", "/bar/*/baz")
    router.addRoute("/bar/*/abc", "/bar/*/abc")
    
    print(router.callRoute('/bar/foo/baz'))
    print(router.callRoute('/bar/abc/baz'))
    print(router.callRoute('/bar/foo/abc'))

    print(router.path_mapping)

    # # test case 1: 
    # print("Test case 1:")
    # assert router.callRoute('/bar') == "Hello bar"    

    # # test case 2: 
    # print("Test case 2:")
    # try:
    #     assert router.callRoute('/random')
    # except Exception as e:
    #     print("Exception raised successfuly")






    

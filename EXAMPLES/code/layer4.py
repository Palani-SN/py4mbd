
from py4mbd.inner import pod

class layer4(pod):

    # Sample Function that gets two input strings, ( inp1, inp2 )
    # Prints them side by side
    # returns nothing (None)
    def dummy(self, inp1:str=None, inp2:str=None):
        """
        model 

        YML format

        - dummy:
            inp1: "Hello"
            inp2: "World"
        
        JSON format

        {
            "dummy": {
                "inp1": "Hello",
                "inp2": "World"
            }
        }

        """
        print("dummy", inp1, inp2)
        return ("dummy", inp1, inp2)
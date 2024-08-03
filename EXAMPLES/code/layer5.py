
from py4mbd.inner import pod

from code.layer6 import layer6

class layer5(pod):

    l6 = layer6()

    # example single_int template function with single argument of type <int>
    def single_int(self, inp_int: int = 0) -> int:
        """
        inp_int is variable of type <int>
        any integer value can be passed for the argument, while the default is 0
        the function returns the same arg value as type <int> 

        model 

            YML format

                - single_int:
                    inp_int: 0
            
            JSON format

                {
                    "single_int": {
                        "inp_int": 0
                    }
                }
        """
        print("inp_int", inp_int)
        return inp_int
    
    # example single_float template function with single argument of type <float>
    def single_float(self, inp_float: float = 0.0) -> float:
        """
        inp_float is variable of type <float>
        any floating point value can be passed for the argument, while the default is 0.0
        the function returns the same arg value as type <float> 

        model 

            YML format

                - single_float:
                    inp_float: 0.0
            
            JSON format

                {
                    "single_float": {
                        "inp_float": 0.0
                    }
                }
        """
        print("inp_float", inp_float)
        return inp_float
    
    # example single_str template function with single argument of type <str>
    def single_str(self, inp_str: str = "None") -> str:
        """
        inp_str is variable of type <str>
        any string value can be passed for the argument, while the default is "None"
        the function returns the same arg value as type <str> 

        model 

            YML format

                - single_str:
                    inp_str: "None"
            
            JSON format

                {
                    "single_str": {
                        "inp_str": "None"
                    }
                }
        """
        print("inp_str", inp_str)
        return inp_str
    
    # example single_list template function with single argument of type <list>
    def single_list(self, inp_list: list = [None]) -> list:
        """
        inp_list is variable of type <list>
        any list value can be passed for the argument, while the default is [None]
        the function returns the same arg value as type <list> 

        model 

            YML format

                - single_list:
                    inp_list: [None]
            
            JSON format

                {
                    "single_list": {
                        "inp_list": [
                            None
                        ]
                    }
                }
        """
        print("inp_list", inp_list)
        return inp_list
    
    # example single_dict template function with single argument of type <dict>
    def single_dict(self, inp_dict: dict = {None:None}) -> dict:
        """
        inp_dict is variable of type <dict>
        any dict value can be passed for the argument, while the default is {None: None}
        the function returns the same arg value as type <dict> 

        model 

            YML format

                - single_dict:
                    inp_dict: {None:None}
            
            JSON format

                {
                    "single_dict": {
                        "inp_dict": {
                            None : None
                        }
                    }
                }
        """
        print("inp_dict", inp_dict)
        return inp_dict
    
    # example single_bool template function with single argument of type <bool>
    def single_bool(self, inp_bool: bool = False) -> bool:
        """
        inp_bool is variable of type <bool>
        any bool value can be passed for the argument, while the default is False
        the function returns the same arg value as type <bool> 

        model 

            YML format

                - single_bool:
                    inp_bool: False
            
            JSON format

                {
                    "single_bool": {
                        "inp_bool": False
                    }
                }
        """
        print("inp_bool", inp_bool)
        return inp_bool
    
    # example multi_args template function with multiple arguments of different types
    def multi_args(self, 
            inp_int: int = 6,
            inp_float: float = 6.3,
            inp_str: str = "Six",
            inp_list: list = [6, 6.3, "Six"],
            inp_dict: dict = {'int': 6, 'float': 6.3, 'str': "Six"},
            inp_bool: bool = False) -> dict:
        """
        Six arguments of different data type can be passed
        any value of the respective data type can be passed for specific argument. for defaults refer above
        the function returns a dict containing all the arguments and its values.

        model 

            YML format

                - multi_args:
                    inp_int: 6
                    inp_float: 6.3
                    inp_str: "Six"
                    inp_list: [6, 6.3, "Six"]
                    inp_dict: {'int': 6, 'float': 6.3, 'str': "Six"}
                    inp_bool: False
            
            JSON format

                {
                    "multi_args": {
                        "inp_int": 6,
                        "inp_float": 6.3,
                        "inp_str": "Six",
                        "inp_list": [6, 6.3, "Six"],
                        "inp_dict": {'int': 6, 'float': 6.3, 'str': "Six"},
                        "inp_bool": False
                    }
                }
        """
        import json
        print("Inputs", json.dumps({
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }, indent=2, sort_keys=False))
        return {
                'inp_int': inp_int,
                'inp_float': inp_float,
                'inp_str': inp_str,
                'inp_list': inp_list,
                'inp_dict': inp_dict,
                'inp_bool': inp_bool
            }
    
    # example raise_err template function for raising an error if negative value is passed in.
    # if positive value is passed in, then it will be returning the same without raising error.
    def raise_err_if_neg(self, 
            inp_int: int = 0) -> int:
        """
        inp_int is variable of type <int>
        any int value (only positive) can be passed for the argument, while the default is 0
        the function returns the same arg value as type <int> 

        model 

            YML format

                - raise_err_if_neg:
                    inp_int: 0
            
            JSON format

                {
                    "raise_err_if_neg": {
                        "inp_int": 0
                    }
                }
        """
        if inp_int < 0:
            raise Exception(f"error: negative values not allowed")
        
        return inp_int
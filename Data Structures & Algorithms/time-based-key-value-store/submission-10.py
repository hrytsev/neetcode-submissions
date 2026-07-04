class TimeMap:

    def __init__(self):
        self.data={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.data.get(key,None):
            self.data[key]=[]
        self.data[key].append({"value":value,"timestamp":timestamp})
        
    def get(self, key: str, timestamp: int) -> str:
        array=self.data.get(key,[])
        if not array:
            return ""
        else:
            l=0
            r=len(array)-1
            res=""
            while l<=r:
                m=(r+l)//2
                if array[m]["timestamp"]<=timestamp:
                    res= array[m]["value"]
                    l=m+1                    
                else:
                    r=m-1

            return res
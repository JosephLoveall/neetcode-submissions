class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for i in strs:
            encoded_string += i
            encoded_string += "??"

        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = List[str]
        decoded_list = s.split("??")
        decoded_list.pop()

        return decoded_list

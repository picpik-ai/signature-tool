import hashlib


class PicpikSigner:
    public_key: str
    private_key: str
    api_key: str

    def __init__(self, public_key: str = "", private_key: str = "", api_key: str = ""):
        self.public_key = public_key
        self.private_key = private_key
        self.api_key = api_key

    def __map_2_string(self, params, exclusive_key: str = None, str_limit: int | None = None):
        content = []
        for key in self.__extract_sorted_keys(params):
            if not exclusive_key or exclusive_key != key:
                content.append(f"{key}{self.__any_2_string(params[key], str_limit)}")
        return "".join(content)

    def __any_2_string(self, v, str_limit: int | None):
        if isinstance(v, bool):
            return self.__simple_2_string(v).lower()
        elif isinstance(v, float) and int(v) == v:
            return self.__simple_2_string(int(v))
        elif isinstance(v, dict):
            return self.__map_2_string(v)
        elif isinstance(v, list):
            return self.__slice_2_string(v, str_limit)
        elif isinstance(v, str):
            return self.__format_string(v, str_limit)
        else:
            return self.__simple_2_string(v)

    def __slice_2_string(self, arr, str_limit: int | None):
        s = ""
        for v in arr:
            s += self.__any_2_string(v, str_limit)
        return s

    def __simple_2_string(self, v):
        if v is None or v == "":
            return ""

        return str(v)

    def __format_string(self, v, limit: int | None):
        if limit and len(v) > limit:
            return v[:limit]

        return v

    def __extract_sorted_keys(self, obj):
        return sorted(obj.keys())

    def sign_service(self, body):
        content = self.__map_2_string(body, "signature", str_limit=128) + self.api_key
        print(content)
        md5_hash = hashlib.md5()
        md5_hash.update(content.encode('utf-8'))
        md5 = md5_hash.hexdigest()
        return md5

    def sign_platform(self, body):
        content = self.__map_2_string(body) + self.private_key
        print(content)
        hashed = hashlib.sha1(content.encode()).hexdigest()
        return hashed

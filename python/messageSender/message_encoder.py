class message_encoder():
    def __init__(self, byteorder='big'):
        self.byteorder = byteorder

    def encode(self, json_messages):
        messages = list()
        for json_message in json_messages["messages"]:
            messages.append(self.encode_message(json_message))
        return messages

    def encode_message(self, json_message):
        message = bytearray()
        for json_field in json_message["fields"]:
            field = self.encode_field(json_field)
            if(self.byteorder == 'big'):
                message += field
            else:
                message = field + message
        return message

    def encode_field(self, json_field):
        field_format = json_field["format"]
        if(field_format == "uint8"):
            return json_field["value"].to_bytes(
                1, self.byteorder, signed=False)
        if(field_format == "uint16"):
            return json_field["value"].to_bytes(
                2, self.byteorder, signed=False)
        if(field_format == "uint32"):
            return json_field["value"].to_bytes(
                4, self.byteorder, signed=False)
        if(field_format == "uint64"):
            return json_field["value"].to_bytes(
                8, self.byteorder, signed=False)
        if(field_format == "int8"):
            return json_field["value"].to_bytes(
                1, self.byteorder, signed=True)
        if(field_format == "int16"):
            return json_field["value"].to_bytes(
                2, self.byteorder, signed=True)
        if(field_format == "int32"):
            return json_field["value"].to_bytes(
                4, self.byteorder, signed=True)
        if(field_format == "int64"):
            return json_field["value"].to_bytes(
                8, self.byteorder, signed=True)
        if(field_format == "string"):
            return json_field["value"].encode("utf-8")

        print("Failed to read field: " + json_field["field_name"])
        return bytes()

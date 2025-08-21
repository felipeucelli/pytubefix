from pytubefix.sabr.proto import BinaryWriter, BinaryReader


class SabrContextSendingPolicy:
    @staticmethod
    def encode(message: dict, writer=None):
        if writer is None:
            writer = BinaryWriter()

        writer.uint32(10).fork()
        for c in message.get("startPolicy", {}):
            writer.uint32(c)

        writer.join()
        writer.uint32(18).fork()
        for c in message.get("stopPolicy", {}):
            writer.uint32(c)

        writer.join()
        writer.uint32(26).fork()
        for c in message.get("discardPolicy", {}):
            writer.uint32(c)

        writer.join()

        return writer

    @staticmethod
    def decode(data, length=None):
        reader = data if isinstance(data, BinaryReader) else BinaryReader(data)
        end = reader.len if length is None else reader.pos + length
        message = dict()

        while reader.pos < end:
            tag = reader.uint32()
            field_number = tag >> 3

            if field_number == 1 and tag == 8:
                message["startPolicy"] = reader.int32()
                continue

            if field_number == 1 and tag == 10:
                end2 = reader.uint32() + reader.pos
                while reader.pos < end2:
                    message["startPolicy"] = reader.int32()
                continue

            if field_number == 2 and tag == 16:
                message["stopPolicy"] = reader.int32()
                continue

            if field_number == 2 and tag == 18:
                end2 = reader.uint32() + reader.pos
                while reader.pos < end2:
                    message["stopPolicy"] = reader.int32()
                continue

            if field_number == 3 and tag == 24:
                message["discardPolicy"] = reader.int32()
                continue

            if field_number == 3 and tag == 26:
                end2 = reader.uint32() + reader.pos
                while reader.pos < end2:
                    message["discardPolicy"] = reader.int32()
                continue


            elif (tag & 7) == 4 or tag == 0:
                break
            else:
                reader.skip(tag & 7)

        return message
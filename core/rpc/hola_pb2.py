# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/rpc/hola.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63ore/rpc/hola.proto\x12\x04hola\"\x07\n\x05\x45mpty\"\x1a\n\nOptionCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x04\"\xde\x05\n\x05\x45vent\x12\x36\n\x12\x46riendRequestEvent\x18\x01 \x01(\x0b\x32\x18.hola.FriendRequestEventH\x00\x12\x34\n\x11GroupRequestEvent\x18\x02 \x01(\x0b\x32\x17.hola.GroupRequestEventH\x00\x12\x38\n\x13PrivateMessageEvent\x18\x03 \x01(\x0b\x32\x19.hola.PrivateMessageEventH\x00\x12\x34\n\x11GroupMessageEvent\x18\x04 \x01(\x0b\x32\x17.hola.GroupMessageEventH\x00\x12:\n\x14\x46riendAddNoticeEvent\x18\x05 \x01(\x0b\x32\x1a.hola.FriendAddNoticeEventH\x00\x12@\n\x17\x46riendRecallNoticeEvent\x18\x06 \x01(\x0b\x32\x1d.hola.FriendRecallNoticeEventH\x00\x12\x42\n\x18GroupIncreaseNoticeEvent\x18\x07 \x01(\x0b\x32\x1e.hola.GroupIncreaseNoticeEventH\x00\x12\x42\n\x18GroupDecreaseNoticeEvent\x18\x08 \x01(\x0b\x32\x1e.hola.GroupDecreaseNoticeEventH\x00\x12>\n\x16GroupRecallNoticeEvent\x18\t \x01(\x0b\x32\x1c.hola.GroupRecallNoticeEventH\x00\x12\x38\n\x13GroupBanNoticeEvent\x18\n \x01(\x0b\x32\x19.hola.GroupBanNoticeEventH\x00\x12<\n\x15GroupAdminNoticeEvent\x18\x0b \x01(\x0b\x32\x1b.hola.GroupAdminNoticeEventH\x00\x12\x30\n\x0fPokeNotifyEvent\x18\x0c \x01(\x0b\x32\x15.hola.PokeNotifyEventH\x00\x42\x07\n\x05\x65vent\"\x82\x03\n\x07Request\x12<\n\x15PrivateMessageRequest\x18\x01 \x01(\x0b\x32\x1b.hola.PrivateMessageRequestH\x00\x12\x38\n\x13GroupMessageRequest\x18\x02 \x01(\x0b\x32\x19.hola.GroupMessageRequestH\x00\x12\x32\n\x10\x44\x65leteMsgRequest\x18\x03 \x01(\x0b\x32\x16.hola.DeleteMsgRequestH\x00\x12,\n\rGetMsgRequest\x18\x04 \x01(\x0b\x32\x13.hola.GetMsgRequestH\x00\x12J\n\x1cSendPrivateForwardMsgRequest\x18\x05 \x01(\x0b\x32\".hola.SendPrivateForwardMsgRequestH\x00\x12\x46\n\x1aSendGroupForwardMsgRequest\x18\x06 \x01(\x0b\x32 .hola.SendGroupForwardMsgRequestH\x00\x42\t\n\x07request\"\xf4\x02\n\x06Result\x12:\n\x14PrivateMessageResult\x18\x01 \x01(\x0b\x32\x1a.hola.PrivateMessageResultH\x00\x12\x36\n\x12GroupMessageResult\x18\x02 \x01(\x0b\x32\x18.hola.GroupMessageResultH\x00\x12\x30\n\x0f\x44\x65leteMsgResult\x18\x03 \x01(\x0b\x32\x15.hola.DeleteMsgResultH\x00\x12*\n\x0cGetMsgResult\x18\x04 \x01(\x0b\x32\x12.hola.GetMsgResultH\x00\x12H\n\x1bSendPrivateForwardMsgResult\x18\x05 \x01(\x0b\x32!.hola.SendPrivateForwardMsgResultH\x00\x12\x44\n\x19SendGroupForwardMsgResult\x18\x06 \x01(\x0b\x32\x1f.hola.SendGroupForwardMsgResultH\x00\x42\x08\n\x06result\"\x8d\x01\n\x06Sender\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x03\x12\x0c\n\x04\x63\x61rd\x18\x05 \x01(\t\x12\x0c\n\x04\x61rea\x18\x06 \x01(\t\x12\r\n\x05level\x18\x07 \x01(\t\x12\x0c\n\x04role\x18\x08 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\"\x9f\x01\n\x05Reply\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x14\n\x0cmessage_type\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\t\x12\x0f\n\x07real_id\x18\x04 \x01(\x03\x12\x1c\n\x06sender\x18\x05 \x01(\x0b\x32\x0c.hola.Sender\x12/\n\x07message\x18\x06 \x03(\x0b\x32\x1e.hola.ReceivableMessageSegment\"3\n\tAnonymous\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x66lag\x18\x03 \x01(\t\"\xfd\x04\n\x18ReceivableMessageSegment\x12(\n\x0bTextSegment\x18\x01 \x01(\x0b\x32\x11.hola.TextSegmentH\x00\x12$\n\tAtSegment\x18\x02 \x01(\x0b\x32\x0f.hola.AtSegmentH\x00\x12(\n\x0b\x46\x61\x63\x65Segment\x18\x03 \x01(\x0b\x32\x11.hola.FaceSegmentH\x00\x12&\n\nRpsSegment\x18\x04 \x01(\x0b\x32\x10.hola.RpsSegmentH\x00\x12(\n\x0b\x44iceSegment\x18\x05 \x01(\x0b\x32\x11.hola.DiceSegmentH\x00\x12*\n\x0cImageSegment\x18\x06 \x01(\x0b\x32\x12.hola.ImageSegmentH\x00\x12,\n\rRecordSegment\x18\x07 \x01(\x0b\x32\x13.hola.RecordSegmentH\x00\x12*\n\x0cVideoSegment\x18\x08 \x01(\x0b\x32\x12.hola.VideoSegmentH\x00\x12\x30\n\x0fLocationSegment\x18\t \x01(\x0b\x32\x15.hola.LocationSegmentH\x00\x12*\n\x0cShareSegment\x18\n \x01(\x0b\x32\x12.hola.ShareSegmentH\x00\x12(\n\x0bJsonSegment\x18\x0b \x01(\x0b\x32\x11.hola.JsonSegmentH\x00\x12&\n\nXmlSegment\x18\x0c \x01(\x0b\x32\x10.hola.XmlSegmentH\x00\x12(\n\x0bPokeSegment\x18\r \x01(\x0b\x32\x11.hola.PokeSegmentH\x00\x12*\n\x0cReplySegment\x18\x0e \x01(\x0b\x32\x12.hola.ReplySegmentH\x00\x42\t\n\x07segment\"W\n\x14GroupMessageResponse\x12\x10\n\x08group_id\x18\x01 \x01(\x03\x12-\n\x07message\x18\x02 \x03(\x0b\x32\x1c.hola.SendibleMessageSegment\"X\n\x16PrivateMessageResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12-\n\x07message\x18\x02 \x03(\x0b\x32\x1c.hola.SendibleMessageSegment\"\xc3\x06\n\x16SendibleMessageSegment\x12(\n\x0bTextSegment\x18\x01 \x01(\x0b\x32\x11.hola.TextSegmentH\x00\x12(\n\x0b\x46\x61\x63\x65Segment\x18\x02 \x01(\x0b\x32\x11.hola.FaceSegmentH\x00\x12*\n\x0cImageSegment\x18\x03 \x01(\x0b\x32\x12.hola.ImageSegmentH\x00\x12,\n\rRecordSegment\x18\x04 \x01(\x0b\x32\x13.hola.RecordSegmentH\x00\x12*\n\x0cVideoSegment\x18\x05 \x01(\x0b\x32\x12.hola.VideoSegmentH\x00\x12$\n\tAtSegment\x18\x06 \x01(\x0b\x32\x0f.hola.AtSegmentH\x00\x12&\n\nRpsSegment\x18\x07 \x01(\x0b\x32\x10.hola.RpsSegmentH\x00\x12(\n\x0b\x44iceSegment\x18\x08 \x01(\x0b\x32\x11.hola.DiceSegmentH\x00\x12(\n\x0bPokeSegment\x18\t \x01(\x0b\x32\x11.hola.PokeSegmentH\x00\x12\x32\n\x10\x41nonymousSegment\x18\n \x01(\x0b\x32\x16.hola.AnonymousSegmentH\x00\x12*\n\x0cShareSegment\x18\x0b \x01(\x0b\x32\x12.hola.ShareSegmentH\x00\x12.\n\x0e\x43ontactSegment\x18\x0c \x01(\x0b\x32\x14.hola.ContactSegmentH\x00\x12\x30\n\x0fLocationSegment\x18\r \x01(\x0b\x32\x15.hola.LocationSegmentH\x00\x12*\n\x0cMusicSegment\x18\x0e \x01(\x0b\x32\x12.hola.MusicSegmentH\x00\x12\x36\n\x12\x43ustomMusicSegment\x18\x0f \x01(\x0b\x32\x18.hola.CustomMusicSegmentH\x00\x12*\n\x0cReplySegment\x18\x10 \x01(\x0b\x32\x12.hola.ReplySegmentH\x00\x12&\n\nXmlSegment\x18\x11 \x01(\x0b\x32\x10.hola.XmlSegmentH\x00\x12(\n\x0bJsonSegment\x18\x12 \x01(\x0b\x32\x11.hola.JsonSegmentH\x00\x42\t\n\x07segment\"\x8c\x01\n\x12\x46riendRequestEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x14\n\x0crequest_type\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x12\x0c\n\x04\x66lag\x18\x07 \x01(\t\"\xaf\x01\n\x11GroupRequestEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x14\n\x0crequest_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x10\n\x08group_id\x18\x06 \x01(\x03\x12\x0f\n\x07user_id\x18\x07 \x01(\x03\x12\x0f\n\x07\x63omment\x18\x08 \x01(\t\x12\x0c\n\x04\x66lag\x18\t \x01(\t\"\xb1\x02\n\x13PrivateMessageEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x14\n\x0cmessage_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x12\n\nmessage_id\x18\x06 \x01(\t\x12\x0f\n\x07user_id\x18\x07 \x01(\x03\x12/\n\x07message\x18\x08 \x03(\x0b\x32\x1e.hola.ReceivableMessageSegment\x12\x13\n\x0braw_message\x18\t \x01(\t\x12\x0c\n\x04\x66ont\x18\n \x01(\x03\x12\x1c\n\x06sender\x18\x0b \x01(\x0b\x32\x0c.hola.Sender\x12\r\n\x05to_me\x18\x0c \x01(\x08\x12\x1a\n\x05reply\x18\r \x01(\x0b\x32\x0b.hola.Reply\"\xe5\x02\n\x11GroupMessageEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x14\n\x0cmessage_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x12\n\nmessage_id\x18\x06 \x01(\t\x12\x10\n\x08group_id\x18\x07 \x01(\x03\x12\x0f\n\x07user_id\x18\x08 \x01(\x03\x12\"\n\tanonymous\x18\t \x01(\x0b\x32\x0f.hola.Anonymous\x12/\n\x07message\x18\n \x03(\x0b\x32\x1e.hola.ReceivableMessageSegment\x12\x13\n\x0braw_message\x18\x0b \x01(\t\x12\x0c\n\x04\x66ont\x18\x0c \x01(\x03\x12\x1c\n\x06sender\x18\r \x01(\x0b\x32\x0c.hola.Sender\x12\r\n\x05to_me\x18\x0e \x01(\x08\x12\x1a\n\x05reply\x18\x0f \x01(\x0b\x32\x0b.hola.Reply\"n\n\x14\x46riendAddNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\x03\"\x85\x01\n\x17\x46riendRecallNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\x03\x12\x12\n\nmessage_id\x18\x06 \x01(\t\"\xab\x01\n\x18GroupIncreaseNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x03\x12\x10\n\x08group_id\x18\x07 \x01(\x03\x12\x13\n\x0boperator_id\x18\x08 \x01(\x03\"\xab\x01\n\x18GroupDecreaseNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x03\x12\x10\n\x08group_id\x18\x07 \x01(\x03\x12\x13\n\x0boperator_id\x18\x08 \x01(\x03\"\xab\x01\n\x16GroupRecallNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\x03\x12\x10\n\x08group_id\x18\x06 \x01(\x03\x12\x13\n\x0boperator_id\x18\x07 \x01(\x03\x12\x12\n\nmessage_id\x18\x08 \x01(\t\"\xb8\x01\n\x13GroupBanNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x03\x12\x10\n\x08group_id\x18\x07 \x01(\x03\x12\x13\n\x0boperator_id\x18\x08 \x01(\x03\x12\x10\n\x08\x64uration\x18\t \x01(\x03\"\x93\x01\n\x15GroupAdminNoticeEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x03\x12\x10\n\x08group_id\x18\x07 \x01(\x03\"\xa0\x01\n\x0fPokeNotifyEvent\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0f\n\x07self_id\x18\x02 \x01(\x03\x12\x11\n\tpost_type\x18\x03 \x01(\t\x12\x13\n\x0bnotice_type\x18\x04 \x01(\t\x12\x10\n\x08sub_type\x18\x05 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\x03\x12\x11\n\ttarget_id\x18\x07 \x01(\x03\x12\x10\n\x08group_id\x18\x08 \x01(\x03\"\x1b\n\x0bTextSegment\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x17\n\tAtSegment\x12\n\n\x02qq\x18\x01 \x01(\t\"\x19\n\x0b\x46\x61\x63\x65Segment\x12\n\n\x02id\x18\x01 \x01(\t\"\x0c\n\nRpsSegment\"\r\n\x0b\x44iceSegment\"Y\n\x0cImageSegment\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\x12\x0f\n\x07timeout\x18\x05 \x01(\t\"L\n\rRecordSegment\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12\x0f\n\x07timeout\x18\x04 \x01(\t\"K\n\x0cVideoSegment\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12\x0f\n\x07timeout\x18\x04 \x01(\t\"K\n\x0fLocationSegment\x12\x0b\n\x03lat\x18\x01 \x01(\t\x12\x0b\n\x03lon\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"J\n\x0cShareSegment\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\"\x1b\n\x0bJsonSegment\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x1a\n\nXmlSegment\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"5\n\x0bPokeSegment\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\x1a\n\x0cReplySegment\x12\n\n\x02id\x18\x01 \x01(\t\"\"\n\x10\x41nonymousSegment\x12\x0e\n\x06ignore\x18\x01 \x01(\x08\"*\n\x0e\x43ontactSegment\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"(\n\x0cMusicSegment\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"m\n\x12\x43ustomMusicSegment\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05\x61udio\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\"[\n\x0f_ForwardSegment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uin\x18\x02 \x01(\t\x12-\n\x07\x63ontent\x18\x03 \x03(\x0b\x32\x1c.hola.SendibleMessageSegment\"W\n\x15PrivateMessageRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12-\n\x07message\x18\x02 \x03(\x0b\x32\x1c.hola.SendibleMessageSegment\"V\n\x13GroupMessageRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x03\x12-\n\x07message\x18\x02 \x03(\x0b\x32\x1c.hola.SendibleMessageSegment\"&\n\x10\x44\x65leteMsgRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\t\"#\n\rGetMsgRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\x03\"W\n\x1cSendPrivateForwardMsgRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12&\n\x07message\x18\x02 \x03(\x0b\x32\x15.hola._ForwardSegment\"V\n\x1aSendGroupForwardMsgRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x03\x12&\n\x07message\x18\x02 \x03(\x0b\x32\x15.hola._ForwardSegment\"*\n\x14PrivateMessageResult\x12\x12\n\nmessage_id\x18\x01 \x01(\t\"(\n\x12GroupMessageResult\x12\x12\n\nmessage_id\x18\x01 \x01(\t\"\x11\n\x0f\x44\x65leteMsgResult\"\x90\x01\n\x0cGetMsgResult\x12\x12\n\nmessage_id\x18\x01 \x01(\x03\x12\x0f\n\x07real_id\x18\x02 \x01(\x03\x12\x1c\n\x06sender\x18\x03 \x01(\x0b\x32\x0c.hola.Sender\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12/\n\x07message\x18\x05 \x03(\x0b\x32\x1e.hola.ReceivableMessageSegment\"1\n\x1bSendPrivateForwardMsgResult\x12\x12\n\nmessage_id\x18\x01 \x01(\t\"/\n\x19SendGroupForwardMsgResult\x12\x12\n\nmessage_id\x18\x01 \x01(\t2\x8d\x01\n\x07\x43hannel\x12.\n\x06option\x12\x10.hola.OptionCode\x1a\x10.hola.OptionCode\"\x00\x12#\n\x05match\x12\x0b.hola.Event\x1a\x0b.hola.Empty\"\x00\x12-\n\x08\x63\x61llBack\x12\x0c.hola.Result\x1a\r.hola.Request\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.rpc.hola_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=29
  _EMPTY._serialized_end=36
  _OPTIONCODE._serialized_start=38
  _OPTIONCODE._serialized_end=64
  _EVENT._serialized_start=67
  _EVENT._serialized_end=801
  _REQUEST._serialized_start=804
  _REQUEST._serialized_end=1190
  _RESULT._serialized_start=1193
  _RESULT._serialized_end=1565
  _SENDER._serialized_start=1568
  _SENDER._serialized_end=1709
  _REPLY._serialized_start=1712
  _REPLY._serialized_end=1871
  _ANONYMOUS._serialized_start=1873
  _ANONYMOUS._serialized_end=1924
  _RECEIVABLEMESSAGESEGMENT._serialized_start=1927
  _RECEIVABLEMESSAGESEGMENT._serialized_end=2564
  _GROUPMESSAGERESPONSE._serialized_start=2566
  _GROUPMESSAGERESPONSE._serialized_end=2653
  _PRIVATEMESSAGERESPONSE._serialized_start=2655
  _PRIVATEMESSAGERESPONSE._serialized_end=2743
  _SENDIBLEMESSAGESEGMENT._serialized_start=2746
  _SENDIBLEMESSAGESEGMENT._serialized_end=3581
  _FRIENDREQUESTEVENT._serialized_start=3584
  _FRIENDREQUESTEVENT._serialized_end=3724
  _GROUPREQUESTEVENT._serialized_start=3727
  _GROUPREQUESTEVENT._serialized_end=3902
  _PRIVATEMESSAGEEVENT._serialized_start=3905
  _PRIVATEMESSAGEEVENT._serialized_end=4210
  _GROUPMESSAGEEVENT._serialized_start=4213
  _GROUPMESSAGEEVENT._serialized_end=4570
  _FRIENDADDNOTICEEVENT._serialized_start=4572
  _FRIENDADDNOTICEEVENT._serialized_end=4682
  _FRIENDRECALLNOTICEEVENT._serialized_start=4685
  _FRIENDRECALLNOTICEEVENT._serialized_end=4818
  _GROUPINCREASENOTICEEVENT._serialized_start=4821
  _GROUPINCREASENOTICEEVENT._serialized_end=4992
  _GROUPDECREASENOTICEEVENT._serialized_start=4995
  _GROUPDECREASENOTICEEVENT._serialized_end=5166
  _GROUPRECALLNOTICEEVENT._serialized_start=5169
  _GROUPRECALLNOTICEEVENT._serialized_end=5340
  _GROUPBANNOTICEEVENT._serialized_start=5343
  _GROUPBANNOTICEEVENT._serialized_end=5527
  _GROUPADMINNOTICEEVENT._serialized_start=5530
  _GROUPADMINNOTICEEVENT._serialized_end=5677
  _POKENOTIFYEVENT._serialized_start=5680
  _POKENOTIFYEVENT._serialized_end=5840
  _TEXTSEGMENT._serialized_start=5842
  _TEXTSEGMENT._serialized_end=5869
  _ATSEGMENT._serialized_start=5871
  _ATSEGMENT._serialized_end=5894
  _FACESEGMENT._serialized_start=5896
  _FACESEGMENT._serialized_end=5921
  _RPSSEGMENT._serialized_start=2077
  _RPSSEGMENT._serialized_end=2089
  _DICESEGMENT._serialized_start=2117
  _DICESEGMENT._serialized_end=2130
  _IMAGESEGMENT._serialized_start=5952
  _IMAGESEGMENT._serialized_end=6041
  _RECORDSEGMENT._serialized_start=6043
  _RECORDSEGMENT._serialized_end=6119
  _VIDEOSEGMENT._serialized_start=6121
  _VIDEOSEGMENT._serialized_end=6196
  _LOCATIONSEGMENT._serialized_start=6198
  _LOCATIONSEGMENT._serialized_end=6273
  _SHARESEGMENT._serialized_start=6275
  _SHARESEGMENT._serialized_end=6349
  _JSONSEGMENT._serialized_start=6351
  _JSONSEGMENT._serialized_end=6378
  _XMLSEGMENT._serialized_start=6380
  _XMLSEGMENT._serialized_end=6406
  _POKESEGMENT._serialized_start=6408
  _POKESEGMENT._serialized_end=6461
  _REPLYSEGMENT._serialized_start=6463
  _REPLYSEGMENT._serialized_end=6489
  _ANONYMOUSSEGMENT._serialized_start=6491
  _ANONYMOUSSEGMENT._serialized_end=6525
  _CONTACTSEGMENT._serialized_start=6527
  _CONTACTSEGMENT._serialized_end=6569
  _MUSICSEGMENT._serialized_start=6571
  _MUSICSEGMENT._serialized_end=6611
  _CUSTOMMUSICSEGMENT._serialized_start=6613
  _CUSTOMMUSICSEGMENT._serialized_end=6722
  __FORWARDSEGMENT._serialized_start=6724
  __FORWARDSEGMENT._serialized_end=6815
  _PRIVATEMESSAGEREQUEST._serialized_start=6817
  _PRIVATEMESSAGEREQUEST._serialized_end=6904
  _GROUPMESSAGEREQUEST._serialized_start=6906
  _GROUPMESSAGEREQUEST._serialized_end=6992
  _DELETEMSGREQUEST._serialized_start=6994
  _DELETEMSGREQUEST._serialized_end=7032
  _GETMSGREQUEST._serialized_start=7034
  _GETMSGREQUEST._serialized_end=7069
  _SENDPRIVATEFORWARDMSGREQUEST._serialized_start=7071
  _SENDPRIVATEFORWARDMSGREQUEST._serialized_end=7158
  _SENDGROUPFORWARDMSGREQUEST._serialized_start=7160
  _SENDGROUPFORWARDMSGREQUEST._serialized_end=7246
  _PRIVATEMESSAGERESULT._serialized_start=7248
  _PRIVATEMESSAGERESULT._serialized_end=7290
  _GROUPMESSAGERESULT._serialized_start=7292
  _GROUPMESSAGERESULT._serialized_end=7332
  _DELETEMSGRESULT._serialized_start=1319
  _DELETEMSGRESULT._serialized_end=1336
  _GETMSGRESULT._serialized_start=7354
  _GETMSGRESULT._serialized_end=7498
  _SENDPRIVATEFORWARDMSGRESULT._serialized_start=7500
  _SENDPRIVATEFORWARDMSGRESULT._serialized_end=7549
  _SENDGROUPFORWARDMSGRESULT._serialized_start=7551
  _SENDGROUPFORWARDMSGRESULT._serialized_end=7598
  _CHANNEL._serialized_start=7601
  _CHANNEL._serialized_end=7742
# @@protoc_insertion_point(module_scope)

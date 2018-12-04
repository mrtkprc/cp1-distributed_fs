# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dfs_pb2 as dfs__pb2


class DFSStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateFile = channel.unary_unary(
        '/dfs.DFS/CreateFile',
        request_serializer=dfs__pb2.CreateFileRequest.SerializeToString,
        response_deserializer=dfs__pb2.CreateFileReply.FromString,
        )
    self.ListDir = channel.unary_unary(
        '/dfs.DFS/ListDir',
        request_serializer=dfs__pb2.ListDirRequest.SerializeToString,
        response_deserializer=dfs__pb2.ListDirReply.FromString,
        )
    self.AppendFile = channel.unary_unary(
        '/dfs.DFS/AppendFile',
        request_serializer=dfs__pb2.AppendFileRequest.SerializeToString,
        response_deserializer=dfs__pb2.AppendFileReply.FromString,
        )
    self.TruncateFile = channel.unary_unary(
        '/dfs.DFS/TruncateFile',
        request_serializer=dfs__pb2.TruncateFileRequest.SerializeToString,
        response_deserializer=dfs__pb2.TruncateFileReply.FromString,
        )
    self.RemoveFile = channel.unary_unary(
        '/dfs.DFS/RemoveFile',
        request_serializer=dfs__pb2.RemoveFileRequest.SerializeToString,
        response_deserializer=dfs__pb2.RemoveFileReply.FromString,
        )
    self.ReadFile = channel.unary_unary(
        '/dfs.DFS/ReadFile',
        request_serializer=dfs__pb2.ReadFileRequest.SerializeToString,
        response_deserializer=dfs__pb2.ReadFileReply.FromString,
        )
    self.DownloadFile = channel.unary_unary(
        '/dfs.DFS/DownloadFile',
        request_serializer=dfs__pb2.DownloadFileRequest.SerializeToString,
        response_deserializer=dfs__pb2.DownloadFileReply.FromString,
        )


class DFSServicer(object):
  """The greeting service definition.
  """

  def CreateFile(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDir(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AppendFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TruncateFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DFSServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateFile': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFile,
          request_deserializer=dfs__pb2.CreateFileRequest.FromString,
          response_serializer=dfs__pb2.CreateFileReply.SerializeToString,
      ),
      'ListDir': grpc.unary_unary_rpc_method_handler(
          servicer.ListDir,
          request_deserializer=dfs__pb2.ListDirRequest.FromString,
          response_serializer=dfs__pb2.ListDirReply.SerializeToString,
      ),
      'AppendFile': grpc.unary_unary_rpc_method_handler(
          servicer.AppendFile,
          request_deserializer=dfs__pb2.AppendFileRequest.FromString,
          response_serializer=dfs__pb2.AppendFileReply.SerializeToString,
      ),
      'TruncateFile': grpc.unary_unary_rpc_method_handler(
          servicer.TruncateFile,
          request_deserializer=dfs__pb2.TruncateFileRequest.FromString,
          response_serializer=dfs__pb2.TruncateFileReply.SerializeToString,
      ),
      'RemoveFile': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveFile,
          request_deserializer=dfs__pb2.RemoveFileRequest.FromString,
          response_serializer=dfs__pb2.RemoveFileReply.SerializeToString,
      ),
      'ReadFile': grpc.unary_unary_rpc_method_handler(
          servicer.ReadFile,
          request_deserializer=dfs__pb2.ReadFileRequest.FromString,
          response_serializer=dfs__pb2.ReadFileReply.SerializeToString,
      ),
      'DownloadFile': grpc.unary_unary_rpc_method_handler(
          servicer.DownloadFile,
          request_deserializer=dfs__pb2.DownloadFileRequest.FromString,
          response_serializer=dfs__pb2.DownloadFileReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dfs.DFS', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

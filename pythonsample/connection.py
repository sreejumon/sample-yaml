import redis


# class Singleton(type):
#     """
#     An metaclass for singleton purpose. Every singleton class should inherit from this class by 'metaclass=Singleton'.
#     """
#     _instances = {}
#  
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#     
#     
# 
# class RedisClient(object):
#     __metaclass__ = Singleton
#     def __init__(self):
#         print("HelloWorld")
#         self.pool = redis.ConnectionPool(host = "localhost", port = 6379)
#     
#     @property
#     def conn(self):
#         if not hasattr(self, '_conn'):
#             self.getConnection()
#         return self._conn
# 
#     def getConnection(self):
#         self._conn = redis.Redis(connection_pool = self.pool)
#         
#         
# if __name__ == '__main__':
#     
#     a = RedisClient()
#     b = RedisClient()
#     c = RedisClient()
#     
#     print(id(a))
#     print(id(b))
#     print(id(c))





class Connections(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host="redis-main-service-1", port = 6379)
        
    def get_client(self):
        return redis.Redis(connection_pool = self.pool)
    


connections = Connections()

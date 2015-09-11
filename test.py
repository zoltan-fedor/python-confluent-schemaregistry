from confluent.schemaregistry.client import CachedSchemaRegistryClient
from confluent.schemaregistry.serializers import MessageSerializer, Util
import types
import avro

# Note that some methods may throw exceptions if
# the registry cannot be reached, decoding/encoding fails,
# or IO fails

# some helper methods in util to get a schema
avro_schema = Util.parse_schema_from_file('/data/apps/python-confluent-schemaregistry/test/basic_schema.avsc')
#avro_schema = Util.parse_schema_from_string(open('/path/to/schema.avsc').read())

def hash_func(self):
    return super.__hash__
avro_schema.__hash__ = types.MethodType( avro.schema.NamedSchema.__hash__, avro_schema)

#print(avro_schema.__hash__())
print('-----------------')


a = {}
print(type(avro_schema))
a.get(avro_schema, -1)

# Initialize the client
client = CachedSchemaRegistryClient(url='http://10.206.74.110:8081')

# Schema operations
print(type(avro_schema))
# register a schema for a subject
schema_id = client.register('test', avro_schema)

# get the latest schema info for a subject
schema_id,avro_schema,schema_version = client.get_latest_schema('test')

print(schema_id)
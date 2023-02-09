from cls import vampire as vo
import utils.json as vjson
import json

test_data = vo.VParam(label="test-param", value="test-value", unit="test-unit")
print(json.dumps(test_data, cls=vjson.VampireEncoder))

test_block = vo.VBlock(label="test-block", params=[test_data])
# print(json.dumps(test_block, cls=vjson.VampireEncoder))
# print(test_block.dumps())

test_input = vo.VInput(label="test-input", blocks=[test_block])
# print(json.dumps(test_input, cls=vjson.VampireEncoder))


test_material = vo.VMaterialBlock(1, [test_data])
test_material_block = vo.VMaterial([test_material])
# print(json.dumps(test_material_block, cls=vjson.VampireEncoder))

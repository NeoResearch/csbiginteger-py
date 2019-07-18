from unittest import TestCase
from csbiginteger.BigInteger import BigInteger as BigIntegerOrig


# The test-cases are copied from neo-python where we use some NEO specific methods
# Extending BigInteger here to add those specific methods
class BigInteger(BigIntegerOrig):
    def __init__(self, *args, **kwargs):
        super(BigInteger, self).__init__(*args, **kwargs)

    def ToByteArray(self):
        return bytearray(self._data)[:self._length]

    def Equals(self, other) -> bool:
        return self.__eq__(other)

    @property
    def Sign(self) -> int:
        if self > 0:
            return 1
        elif self == 0:
            return 0
        return -1


class BigIntegerTestCase(TestCase):
    def test_big_integer_add(self):
        b1 = BigInteger(10)
        b2 = BigInteger(20)

        b3 = b1 + b2

        self.assertIsInstance(b3, BigInteger)
        self.assertEqual(b3, 30)

    def test_big_integer_sub(self):
        b1 = BigInteger(5505505505505505050505)
        b2 = BigInteger(5505505505505505000000)

        b3 = b1 - b2

        self.assertIsInstance(b3, BigInteger)
        self.assertEqual(b3, 50505)

    def test_big_integer_mul(self):
        b1 = BigInteger(55055055055055)
        b2 = BigInteger(55055055055)

        b3 = b1 * b2

        self.assertIsInstance(b3, BigInteger)
        self.assertEqual(b3, 3031059087112109081053025)

    def test_big_integer_div(self):
        b1 = BigInteger(55055055055055)
        b2 = BigInteger(55055055)

        b3 = b1 / b2
        self.assertIsInstance(b3, BigInteger)
        self.assertEqual(b3, 1000000)

    def test_big_integer_div_rounding(self):
        b1 = BigInteger(1)
        b2 = BigInteger(2)
        self.assertEqual(0, b1 / b2)  # 0.5 -> 0

        b1 = BigInteger(2)
        b2 = BigInteger(3)
        self.assertEqual(0, b1 / b2)  # 0.66 -> 0

        b1 = BigInteger(5)
        b2 = BigInteger(4)
        self.assertEqual(1, b1 / b2)  # 1.25 -> 1

        b1 = BigInteger(5)
        b2 = BigInteger(3)
        self.assertEqual(1, b1 / b2)  # 1.66 -> 1

        b1 = BigInteger(-1)
        b2 = BigInteger(3)
        self.assertEqual(0, b1 / b2)  # -0.33 -> 0

        b1 = BigInteger(-5)
        b2 = BigInteger(3)
        self.assertEqual(-1, b1 / b2)  # -1.66 -> -1


    def test_big_integer_div2(self):
        b1 = BigInteger(41483775933600000000)
        b2 = BigInteger(414937759336)

        b3 = b1 / b2
        b4 = b1 // b2
        self.assertIsInstance(b3, BigInteger)
        self.assertEqual(b3, 99975899)
        self.assertEqual(b4, b3)

    def test_big_integer_div_block1473972(self):
        b1 = BigInteger(-11001000000)
        b2 = BigInteger(86400)
        result = b1 / b2
        self.assertEqual(-127326, result)

    def test_big_integer_float(self):
        b1 = BigInteger(5505.001)
        b2 = BigInteger(55055.999)

        b3 = b1 + b2

        self.assertIsInstance(b3, BigInteger)
        self.assertEqual(b3, 60560)

    def test_big_integer_to_ba(self):
        b1 = BigInteger(8972340892734890723)
        ba = b1.ToByteArray()

        integer = BigInteger.from_bytes(ba, 'little')
        self.assertEqual(integer, 8972340892734890723)

        b2 = BigInteger(-100)
        b2ba = b2.ToByteArray()
        integer2 = BigInteger.from_bytes(b2ba, 'little', signed=True)
        self.assertEqual(integer2, -100)

        b3 = BigInteger(128)
        b3ba = b3.ToByteArray()
        self.assertEqual(b3ba, b'\x80\x00')

        b4 = BigInteger(0)
        b4ba = b4.ToByteArray()
        self.assertEqual(b4ba, b'\x00')

        b5 = BigInteger(-146)
        b5ba = b5.ToByteArray()
        self.assertEqual(b'\x6e\xff', b5ba)

        b6 = BigInteger(-48335248028225339427907476932896373492484053930)
        b6ba = b6.ToByteArray()
        self.assertEqual(20, len(b6ba))

        b7 = BigInteger(-399990000)
        b7ba = b7.ToByteArray()
        self.assertEqual(b'\x10\xa3\x28\xe8', b7ba)

    def test_big_integer_frombytes(self):
        b1 = BigInteger(8972340892734890723)
        ba = b1.ToByteArray()

        b2 = BigInteger.from_bytes(ba)
        self.assertEqual(b1, b2)
        self.assertTrue(b1.Equals(b2))

    def test_big_integer_sign(self):
        b1 = BigInteger(3)
        b2 = BigInteger(0)
        b3 = BigInteger(-4)
        self.assertEqual(b1.Sign, 1)
        self.assertEqual(b2.Sign, 0)
        self.assertEqual(b3.Sign, -1)

        c1 = BigInteger(-100)
        c1_bytes = c1.ToByteArray()

        c2 = BigInteger.from_bytes(c1_bytes, signed=True)
        self.assertEqual(c2.Sign, -1)

    def test_big_integer_modulo(self):
        b1 = BigInteger(860593)
        b2 = BigInteger(-201)
        self.assertEqual(112, b1 % b2)

        b1 = BigInteger(20195283520469175757)
        b2 = BigInteger(1048576)
        self.assertEqual(888269, b1 % b2)

        b1 = BigInteger(-18224909727634776050312394179610579601844989529623334093909233530432892596607)
        b2 = BigInteger(14954691977398614017)
        self.assertEqual(-3100049211437790421, b1 % b2)

    def test_dunder_methods(self):
        b1 = BigInteger(1)
        b2 = BigInteger(2)
        b3 = BigInteger(3)

        self.assertEqual(abs(b1), 1)
        self.assertEqual(b1 % 1, 0)
        self.assertEqual(-b1, -1)
        self.assertEqual(str(b1), "1")
        self.assertEqual(b3 // b2, 1)

        right_shift = b3 >> b1
        self.assertEqual(right_shift, 1)
        self.assertIsInstance(right_shift, BigInteger)

        left_shift = b1 << b3
        self.assertEqual(left_shift, 8)
        self.assertIsInstance(left_shift, BigInteger)

    def test_negative_shifting(self):
        # C#'s BigInteger changes a left shift with a negative shift index,
        # to a right shift with a positive index.

        b1 = BigInteger(8)
        b2 = BigInteger(-3)
        # shift against BigInteger
        self.assertEqual(1, b1 << b2)
        # shift against integer
        self.assertEqual(1, b1 << -3)

        # the same as above but for right shift
        self.assertEqual(64, b1 >> b2)
        self.assertEqual(64, b1 >> -3)


using System;
using System.Numerics;
using System.Globalization; // NumberStyles
using System.Collections.Generic; // IEnumerable
using System.Text; // StringBuilder


namespace csbiglib
{
    public class BigIntegerLib
    {
        public BigInteger zero()
        {
            return new BigInteger(0);
        }

        public BigInteger from_int32(int x)
        {
            return new BigInteger(x);
        }

        public BigInteger from_int64(long x)
        {
            return new BigInteger(x);
        }

        public BigInteger to_int32(BigInteger big)
        {
            return (int)big;
        }

        public BigInteger to_int64(BigInteger big)
        {
            return (long)big;
        }

        public BigInteger from_bytes(byte[] x)
        {
            return new BigInteger(x);
        }

        public byte[] to_bytes(BigInteger big)
        {
            return big.ToByteArray();
        }

        public BigInteger from_string(string x, int b)
        {
            if (b == 10)
                return BigInteger.Parse(x);
            // assuming base 16 (bigendian '0x prefixed')
            // small or poor formatted (do not raise exception)
            if ((x.Length < 2) || (x.Length % 2 == 1))
                return new BigInteger(0);
            if ((x.Substring(0, 2) == "0x") || (x.Substring(0, 2) == "0X"))
                x = x.Substring(2, x.Length - 2);
            byte[] bigend = Helper.HexToBytes(x);
            Array.Reverse(bigend, 0, bigend.Length);
            return new BigInteger(bigend); // now is little endian
        }

        public string to_string(BigInteger big, int b)
        {
            if (b == 10)
            {
                return big.ToString();
            }
            // assume base 16
            byte[] little = big.ToByteArray();
            Array.Reverse(little, 0, little.Length); // now bigendian
            return "0x" + Helper.ToHexString(little);
        }
    }
}

public class Helper
{
    public static byte[] HexToBytes(string value)
    {
        if (value == null || value.Length == 0)
            return new byte[0];
        if (value.Length % 2 == 1)
            throw new FormatException();
        byte[] result = new byte[value.Length / 2];
        for (int i = 0; i < result.Length; i++)
            result[i] = byte.Parse(value.Substring(i * 2, 2), NumberStyles.AllowHexSpecifier);
        return result;
    }

    public static string ToHexString(IEnumerable<byte> value)
    {
        StringBuilder sb = new StringBuilder();
        foreach (byte b in value)
            sb.AppendFormat("{0:x2}", b);
        return sb.ToString();
    }
}

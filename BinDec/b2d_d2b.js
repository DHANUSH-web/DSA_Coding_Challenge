const decimal = (binary) =>
{
    let sz, dec = 0, index;
    sz = binary.length;
    index = sz - 1;

    for (let bit of binary)
    {
        if (bit == '1')
        {
            dec += Math.pow(2, index);
        }

        index--;
    }

    return dec;
}

const binary = (dec) =>
{
    let bits = "", bin = "";

    while (dec > 0)
    {
        bits += (dec % 2);
        dec = parseInt(dec / 2);
    }

    for (let i = bits.length-1; i >= 0; i--)
    {
        bin += bits[i];
    }

    return bin;
}

let mode = 'b';

if (mode == 'b')
{
    let b = "11001";
    console.log(`Decimal: ${decimal(b)}`);
}

else
{
    let dec = 25;
    console.log(`Binary: ${binary(dec)}`);
}

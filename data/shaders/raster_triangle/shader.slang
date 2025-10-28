
struct IN_VERTEX
{
}

struct OUT_VERTEX
{

}

struct OUT_PIXEL


[shader("vertex")]
OUT_VERTEX mainVertex(IN_VERTEX in_args)
{
    float4 res;
    return res;
}

[shader("fragment")]
OUT_PIXEL mainPixel(OUT_VERTEX in_args)
{
    return float4();
}
// This function helps to find the x and y absolute coordinates of an element in a webpage.
function getOffset(el)
{
    var _x = 0;
    var _y = 0;
    while( el && !isNaN( el.offsetLeft ) && !isNaN( el.offsetTop ))
    {
        _x += el.offsetLeft - el.scrollLeft;
        _y += el.offsetTop - el.scrollTop;
        el = el.offsetParent;
    }
    return {top:_y, left:_x};
}
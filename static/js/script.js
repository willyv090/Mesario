document.addEventListener('DOMContentLoaded', function () {
    var namePath = document.getElementById('namePath');
    var length = namePath.getTotalLength();
    namePath.style.strokeDasharray = length;
    namePath.style.strokeDashoffset = length;
    namePath.animate(
        [
            { strokeDashoffset: length },
            { strokeDashoffset: 0 }
        ],
        {
            duration: 4000, 
            easing: 'ease',
            fill: 'forwards'
        }
    );
});

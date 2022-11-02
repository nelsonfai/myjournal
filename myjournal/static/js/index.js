mobiscroll.setOptions({
    locale: mobiscroll.localeDe,
    theme: 'ios',
    themeVariant: 'light'
});

var activities = [{
        date: '2022-10-17T00:00',
        move: 200,
        exercise: 360,
        stand: 180
    }, {
        date: '2022-10-18T00:00',
        move: 360,
        exercise: 150,
        stand: 230
    }, {
        date: '2022-10-19T00:00',
        move: 180,
        exercise: 200,
        stand: 280
    }, {
        date: '2022-10-20T00:00',
        move: 120,
        exercise: 150,
        stand: 200
    }, {
        date: '2022-10-21T00:00',
        move: 320,
        exercise: 180,
        stand: 100
    }, {
        date: '2022-10-22T00:00',
        move: 120,
        exercise: 100,
        stand: 200
    }, {
        date: '2022-10-23T00:00',
        move: 230,
        exercise: 170,
        stand: 330
    }, {
        date: '2022-10-24T00:00',
        move: 320,
        exercise: 260,
        stand: 80
    }, {
        date: '2022-10-25T00:00',
        move: 200,
        exercise: 140,
        stand: 180
    }, {
        date: '2022-10-26T00:00',
        move: 360,
        exercise: 300,
        stand: 160
    }, {
        date: '2022-10-27T00:00',
        move: 80,
        exercise: 360,
        stand: 360
    }, {
        date: '2022-10-28T00:00',
        move: 220,
        exercise: 170,
        stand: 290
    }, {
        date: '2022-10-29T00:00',
        move: 120,
        exercise: 40,
        stand: 100
    }, {
        date: '2022-10-30T00:00',
        move: 120,
        exercise: 200,
        stand: 80
    }];

mobiscroll.datepicker('#demo-activity-calendar', {
    controls: ['calendar'],
    touchUi: true,
    display: 'inline',
    renderDayContent: function (args) {
        var a = activities.find(function (obj) { return +new Date(obj.date) === +args.date });

        function getDeg(nr) {
            return {
                rotate1: nr > 180 ? 180 : nr,
                rotate2: nr > 180 ? nr - 180 : 0
            }
        }

        function getStyle(rotate) {
            return ' style="transform: rotateZ(' + rotate + 'deg)"';
        }

        return '<div class="screen">' +
            '<div class="' + (a ? 'dial move' : '') + '">' +
            '<div class="dial-background"' + (a ? ' style="background:#752a2a"' : '') + '></div>' +
            '<div class="dial-container container1">' +
            '<div class="wedge"' + (a ? getStyle(getDeg(a.move).rotate1) : '') + '></div>' +
            '</div>' +
            '<div class="dial-container container2">' +
            '<div class="wedge"' + (a ? getStyle(getDeg(a.move).rotate2) : '') + '></div>' +
            '</div>' +
            '<div class="marker start"></div>' +
            '<div class="marker end"' + (a ? getStyle(a.move) : '') + '></div>' +
            '</div>' +
            '<div class="' + (a ? 'dial exercise' : '') + '">' +
            '<div class="dial-background"' + (a ? ' style="background:#4a6915"' : '') + '></div>' +
            '<div class="dial-container container1">' +
            '<div class="wedge"' + (a ? getStyle(getDeg(a.exercise).rotate1) : '') + '></div>' +
            '</div>' +
            '<div class="dial-container container2">' +
            '<div class="wedge"' + (a ? getStyle(getDeg(a.exercise).rotate2) : '') + '></div>' +
            '</div>' +
            '<div class="marker start"></div>' +
            '<div class="marker end"' + (a ? getStyle(a.exercise) : '') + '></div>' +
            '</div>' +
            '<div class="' + (a ? 'dial stand' : '') + '">' +
            '<div class="dial-background"' + (a ? ' style="background:#157b76"' : '') + '></div>' +
            '<div class="dial-container container1">' +
            '<div class="wedge"' + (a ? getStyle(getDeg(a.stand).rotate1) : '') + '></div>' +
            '</div>' +
            '<div class="dial-container container2">' +
            '<div class="wedge"' + (a ? getStyle(getDeg(a.stand).rotate2) : '') + '></div>' +
            '</div>' +
            '<div class="marker start"></div>' +
            '<div class="marker end"' + (a ? getStyle(a.stand) : '') + '></div>' +
            '</div>' +
            '</div>';
    },
});
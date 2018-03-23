(function($) {
"use strict";

   var chartData = [
    {
        "date": "2018-01-01",
        "receita": 0.00,
        "associations": 0,
        "upgrade": 5,
        "levelName": ""        
    },
    {
        "date": "2018-02-01"        
    },
    {
        "date": "2018-03-01"
    },
    {
        "date": "2018-04-01"
    },
    {
        "date": "2018-05-01"
    },
    {
        "date": "2018-06-01"
    },
    {
        "date": "2018-07-01"
    },
    {
        "date": "2018-08-01"
    },
    {
        "date": "2018-09-01"
    },
    {
        "date": "2018-10-01"
    },
    {
        "date": "2018-11-01"
    },
    {
        "date": "2018-12-01"    
    }
];
var chart = AmCharts.makeChart("chartdiv1", {
  type: "serial",
  theme: "dark",
  dataDateFormat: "YYYY-MM-DD",
  dataProvider: chartData,

  addClassNames: true,
  startDuration: 1,
  color: "#676a6c",
  marginLeft: 0,

  categoryField: "date",
  categoryAxis: {
    parseDates: true,
    minPeriod: "MM",
    autoGridCount: false,
    gridCount: 50,
    gridAlpha: 0.1,
    gridColor: "#676a6c",
    axisColor: "#00bcd4",
    dateFormats: [{
        period: 'DD',
        format: 'DD'
    }, {
        period: 'WW',
        format: 'MMM DD'
    }, {
        period: 'MM',
        format: 'MMM'
    }, {
        period: 'YYYY',
        format: 'YYYY'
    }]
  },

  valueAxes: [{
    id: "a1",
    title: "Receita",
    gridAlpha: 0,
    axisAlpha: 0
  },{
    id: "a2",
    title: "Associações",
    position: "right",
    gridAlpha: 0,
    axisAlpha: 0,
    labelsEnabled: true
  }],
  graphs: [{
    id: "g1",
    valueField:  "receita",
    title:  "Receita (Descontos + Participação)",
    type:  "column",
    fillAlphas:  0.9,
    valueAxis:  "a1",
    balloonText:  "R$ [[value]]",
    legendxPeriodValueText:  "Total: R$ [[value.sum]]",
    lineColor:  "#00bcd4",
    alphaField:  "alpha",
  },{
    id: "g2",
    valueField: "associations",
    classNameField: "bulletClass",
    title: "Associações",
    type: "line",
    valueAxis: "a2",
    lineColor: "#ff7588",
    lineThickness: 1,
    bullet: "round",
    bulletSizeField: "upgrade",
    bulletBorderColor: "#ff7588",
    bulletBorderAlpha: 1,
    bulletBorderThickness: 2,
    bulletColor: "#ff7588",
    labelText: "[[levelName]]",
    labelPosition: "right",
    balloonText: "Associações: [[value]]",
    showBalloon: true,
    animationPlayed: true,
  }],

  chartCursor: {
    zoomable: false,
    categoryBalloonDateFormat: "DD",
    cursorAlpha: 0,
    valueBalloonsEnabled: false
  },
  legend: {
    bulletType: "round",
    equalWidths: false,
    valueWidth: 120,
    useGraphSettings: true,
    color: "#00bcd4"
  }
});

// Flexible table
var table = $('#proList').DataTable({
"bPaginate": true,
"bLengthChange": false,
"bFilter": true,
"bInfo": false,
"bAutoWidth": false });
//  external search bar
$('#search-projects').on( 'keyup', function () {
    table.search( this.value ).draw();
} );

$('#drop-remove').iCheck({
                checkboxClass: 'icheckbox_square-blue',
                radioClass: 'iradio_square-blue'
            });

})(jQuery);
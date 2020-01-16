
const xlabels = [];
const xaccel = [];
const yaccel = [];
const zaccel = [];

var timeStart = 0;

var arraySize = 20;

//chartIt();
//updateChart();


const ctx = document.getElementById('chart').getContext('2d');
const chart = new Chart(ctx,{
	type: 'line',
	data: {
		labels: xlabels,//[0],
		datasets: [
		{
			label: 'X - Axis',
			data: xaccel,//[0],
			backgroundColor: 'rgba(128, 182, 244, 0.2)',
			borderColor: 'rgba(128, 182, 244, 1)',
			borderWidth: 1
		},
		{
			label: 'Y - Axis',
			data: yaccel,//[0],
			backgroundColor: 'rgba(179,181,198,0.2)',
			borderColor: 'rgba(179,181,198,1)',
			borderWidth: 1
		},
		{
			label: 'Z - Axis',
			data: zaccel,//[0],
			backgroundColor: 'rgba(255, 99, 132, 0.2)',
			borderColor: 'rgba(255, 99, 132, 1)',
			borderWidth: 1
		}
		]
	},
	    options: {
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true,
					display: false
                }
            }]
        }
    }

});



async function updateChart(data){
	//var currentTime = new Date();
	//currentTime = currentTime.getSeconds();
	timeStart = timeStart + 0.2;
	chart.data.labels.push(timeStart);
	chart.data.datasets[0].data.push(data.getUint8(0));
	chart.data.datasets[1].data.push(data.getUint8(1));
	chart.data.datasets[2].data.push(data.getUint8(2));
	
	chart.update();
	
	
	
	if(arraySize < 35) arraySize++;
	else
	{
		xlabels.shift(); //removes oldest data point
		xaccel.shift();
		yaccel.shift();
		zaccel.shift();
	}
    //chart.update();
	//xlabels.push(timeStart);
	//xaccel.push(data.getUint8(0));
	//yaccel.push(data.getUint8(1));
	//zaccel.push(data.getUint8(2));
	
}

const techniqueRange = document.querySelector('#technique');
const feelingRange = document.querySelector('#feeling');
const timeRange = document.querySelector('#time');
const soloingRange = document.querySelector('#soloing');
const attitudeRange = document.querySelector('#attitude');

const techniqueValue = document.querySelector('#technique-value');
const feelingValue = document.querySelector('#feeling-value');
const timeValue = document.querySelector('#time-value');
const soloingValue = document.querySelector('#soloing-value');
const attitudeValue = document.querySelector('#attitude-value');


techniqueRange.oninput = function() {
    techniqueValue.innerHTML = this.value;
};

feelingRange.oninput = function() {
    feelingValue.innerHTML = this.value;
};

timeRange.oninput = function() {
    timeValue.innerHTML = this.value;
};

soloingRange.oninput = function() {
    soloingValue.innerHTML = this.value;
};

attitudeRange.oninput = function() {
    attitudeValue.innerHTML = this.value;
};
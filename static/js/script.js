function showSection(sectionId) {

    document.getElementById("dashboard").style.display = "none";
    document.getElementById("incidents").style.display = "none";
    document.getElementById("intel").style.display = "none";
    document.getElementById("playbook").style.display = "none";

    document.getElementById(sectionId).style.display = "block";
}

function updateClock(){

    let now = new Date();

    document.getElementById("clock").innerHTML =
    now.toLocaleTimeString();

}

setInterval(updateClock,1000);

updateClock();

const pieChart = document.getElementById('pieChart');

if(pieChart){

new Chart(pieChart,{

type:'pie',

data:{

labels:['Brute Force','Malware','SQL Injection','Phishing'],

datasets:[{

data:[35,25,20,20]

}]

}

});

}

const barChart=document.getElementById('barChart');

if(barChart){

new Chart(barChart,{

type:'bar',

data:{

labels:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],

datasets:[{

label:'Detected Attacks',

data:[18,25,12,31,26,14,22]

}]

}

});

}

function runPlaybook(){

    document.getElementById("playbookModal").style.display="flex";

}

function closePlaybook(){

    document.getElementById("playbookModal").style.display="none";

}

function viewReports(){

    document.querySelector(".charts").scrollIntoView({

        behavior:"smooth"

    });

}

const activities = [

"🚨 Brute Force Attack Detected",

"🛡 Source IP Blocked",

"🌍 Threat Intelligence Updated",

"🔒 Endpoint Successfully Isolated",

"📧 Security Team Notified",

"⚙ Firewall Rule Applied",

"✅ Playbook Executed Successfully"

];

let activityIndex = 0;

setInterval(function(){

const feed=document.getElementById("activityFeed");

if(feed){

const li=document.createElement("li");

li.innerHTML=activities[activityIndex];

feed.prepend(li);

activityIndex++;

if(activityIndex>=activities.length){

activityIndex=0;

}

if(feed.children.length>6){

feed.removeChild(feed.lastChild);

}

}

},4000);

function animateCounter(id, target){

let count=0;

const speed=Math.ceil(target/80);

const element=document.getElementById(id);

const timer=setInterval(function(){

count+=speed;

if(count>=target){

count=target;

clearInterval(timer);

}

element.innerHTML=count;

},20);

}

window.onload=function(){

animateCounter("alerts",247);

animateCounter("critical",18);

animateCounter("malicious",52);

animateCounter("blocked",46);

}
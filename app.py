
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CELL TYCOON",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}
.stApp {background:#fff;}
.block-container {padding:0!important;max-width:100%!important;}
iframe {border:0!important;}
</style>
""", unsafe_allow_html=True)

GAME = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

* {box-sizing:border-box}
body {margin:0;background:#fff;color:#292333;font-family:'Press Start 2P',monospace}
button {font-family:inherit;cursor:pointer;user-select:none;-webkit-tap-highlight-color:transparent}

/* ALL BUTTONS */
.pixel-btn {
    border:4px solid #171421;
    box-shadow:0 7px 0 #171421,0 10px 12px #0003;
    transition:transform .10s ease,box-shadow .10s ease,filter .12s;
    position:relative;
}
.pixel-btn:hover {filter:brightness(1.16)}
.pixel-btn:active,.pixel-btn.pressed {
    transform:translateY(6px) scale(.98);
    box-shadow:0 1px 0 #171421,0 3px 5px #0003;
}
.pixel-btn:disabled {opacity:.55;cursor:not-allowed;filter:grayscale(.5)}
.upgrade-btn:active,.upgrade-btn.pressed {
    transform:translateY(4px) scale(.98);
    box-shadow:none;
}

/* GAME BACKGROUND */
#game {
    width:100%;
    min-height:950px;
    position:relative;
    overflow:hidden;
    background-color:#fff;
    background-image:
        linear-gradient(#d6d6d6 2px,transparent 2px),
        linear-gradient(90deg,#d6d6d6 2px,transparent 2px);
    background-size:60px 60px;
}
#topbar {
    height:65px;background:#292433;color:white;
    display:flex;align-items:center;justify-content:space-between;
    padding:0 20px;position:relative;z-index:3;gap:10px;
}
#brand {font-size:16px;color:#ff5656;text-shadow:3px 3px #111}
.topstat {font-size:10px;line-height:2}
.green {color:#5aff78}
.gold {color:#ffd15c}

/* LEFT MENU */
#left {
    position:absolute;left:15px;top:105px;
    display:flex;flex-direction:column;gap:18px;z-index:4;
}
.side-btn {
    width:105px;height:85px;background:#332d40;color:white;
    font-size:9px;display:flex;align-items:center;
    justify-content:center;flex-direction:column;gap:8px;
}
.side-icon {font-size:32px}

/* TOP MENU */
#skillBtn,#moreBtn {
    position:absolute;top:85px;width:125px;height:90px;
    background:#302b3c;color:white;font-size:10px;line-height:2;z-index:4;
}
#skillBtn {left:50%;transform:translateX(-65%)}
#skillBtn:active,#skillBtn.pressed {transform:translateX(-65%) translateY(6px) scale(.98)}
#moreBtn {left:calc(50% + 80px);background:#eab63b;color:#292333}

/* CELL AREA */
#center {
    position:absolute;left:50%;top:210px;transform:translateX(-50%);
    width:min(650px,70%);min-height:350px;
    display:flex;align-content:center;align-items:center;
    justify-content:center;flex-wrap:wrap;gap:30px;padding:25px;
    overflow:visible;
}
.ball {
    width:125px;height:125px;border-radius:37%;
    background:var(--ball);border:12px solid var(--dark);
    position:relative;flex:0 0 auto;
    box-shadow:inset 9px 9px 0 var(--light),
               inset -10px -12px 0 var(--dark),
               8px 13px 15px #0003;
    animation:float 2s ease-in-out infinite alternate;
}
.ball:after {
    content:"";position:absolute;width:42px;height:12px;
    background:#ffffff77;left:15px;top:12px;
    border-radius:10px;transform:rotate(-35deg);
}
@keyframes float {
    from {transform:translateY(-4px)}
    to {transform:translateY(5px)}
}

/* SPLITTING DAUGHTER CELLS */
.split-overlay {
    position:absolute;inset:0;pointer-events:none;z-index:8;
}
.split-daughter {
    position:absolute;width:125px;height:125px;border-radius:37%;
    border:12px solid var(--dark);background:var(--ball);
    box-shadow:inset 9px 9px 0 var(--light),
               inset -10px -12px 0 var(--dark),8px 13px 15px #0003;
    transform-origin:center;
}
.split-daughter:after {
    content:"";position:absolute;width:42px;height:12px;
    background:#ffffff77;left:15px;top:12px;
    border-radius:10px;transform:rotate(-35deg);
}
@keyframes daughterLeft {
    0% {transform:translate(0,0) scale(.08,.9);opacity:.5}
    15% {transform:translate(-8px,0) scale(.75,1.05);opacity:1}
    100% {transform:translate(-65px,-12px) scale(1);opacity:1}
}
@keyframes daughterRight {
    0% {transform:translate(0,0) scale(.08,.9);opacity:.5}
    15% {transform:translate(8px,0) scale(.75,1.05);opacity:1}
    100% {transform:translate(65px,12px) scale(1);opacity:1}
}
.split-daughter.left {animation:daughterLeft var(--duration) cubic-bezier(.2,.8,.2,1) forwards}
.split-daughter.right {animation:daughterRight var(--duration) cubic-bezier(.2,.8,.2,1) forwards}
.split-parent {opacity:0!important}

/* SELL ANIMATION */
.selling-ball {
    animation:sellAway var(--duration) ease-in forwards!important;
}
@keyframes sellAway {
    0% {transform:scale(1);opacity:1}
    35% {transform:scale(1.15);opacity:1}
    100% {transform:scale(.05);opacity:0}
}

/* STATS AND UPGRADES */
#stats {
    position:absolute;top:305px;right:18px;width:245px;
    display:flex;flex-direction:column;gap:12px;z-index:2;
}
.stat {
    background:#2c2736;color:#f5e9ce;border:5px solid #171421;
    box-shadow:5px 5px 0 #171421;padding:13px 11px;
    min-height:86px;font-size:9px;line-height:2;
}
.stat-head {display:flex;justify-content:space-between;gap:5px;margin-bottom:8px}
.price {color:#54f17a}
.upgrade-btn {
    width:100%;background:transparent;border:0;
    color:#eee4ca;font-family:inherit;font-size:9px;
    text-align:left;padding:0;line-height:2.1;
    box-shadow:none;transition:transform .1s ease,color .1s;
}
.upgrade-btn:hover {color:#ffd15b;filter:none}

/* BOTTOM BUTTONS */
#bottom {
    position:absolute;bottom:65px;left:50%;transform:translateX(-50%);
    width:min(850px,90%);display:flex;gap:20px;z-index:4;
}
.big-btn {
    flex:1;height:120px;background:#383145;color:#fff0d0;font-size:21px;
}
#sellBtn {background:#285d40}
#splitInfo {position:absolute;top:-35px;left:19%;font-size:17px;color:#292333;text-shadow:2px 2px white}
#cooldown {position:absolute;top:-22px;right:10%;color:#292333;font-size:8px}

/* NOTIFICATIONS */
#message {
    display:none;position:absolute;z-index:20;top:245px;left:50%;
    transform:translateX(-50%);background:#302a3d;color:white;
    padding:16px;font-size:10px;line-height:2;text-align:center;
    max-width:85%;box-shadow:4px 4px #111;
}
.coin-float {
    position:absolute;color:#30b954;font-size:13px;
    pointer-events:none;z-index:30;animation:coinUp 1s forwards;
}
@keyframes coinUp {
    from {opacity:1;transform:translateY(0)}
    to {opacity:0;transform:translateY(-85px)}
}

/* MENUS */
#modal {
    display:none;position:fixed;inset:0;background:#0009;z-index:100;
    align-items:center;justify-content:center;padding:15px;
}
#modalBox {
    width:min(650px,96%);max-height:85vh;overflow-y:auto;
    background:#302b3d;color:#fff0d0;border:6px solid #171421;
    box-shadow:9px 9px #0008;padding:20px;
    animation:modalIn .2s ease;
}
@keyframes modalIn {
    from {transform:scale(.85);opacity:0}
    to {transform:scale(1);opacity:1}
}
#modalTitle {font-size:15px;color:#ffd15c;margin-bottom:20px;line-height:2}
.modal-item {
    border:3px solid #756b83;padding:14px;margin:11px 0;
    display:flex;align-items:center;justify-content:space-between;
    gap:10px;font-size:9px;line-height:2.2;
}
.modal-item button {
    background:#4b9861;color:white;padding:12px;
    border:3px solid #171421;box-shadow:0 5px 0 #171421;
    font-size:8px;white-space:nowrap;
    transition:transform .1s,box-shadow .1s;
}
.modal-item button:active {
    transform:translateY(4px);box-shadow:0 1px #171421;
}
.close-btn {
    background:#c44949;color:white;padding:13px;margin-top:15px;
    border:3px solid #171421;box-shadow:0 5px #171421;font-size:9px;
}
.close-btn:active {transform:translateY(4px);box-shadow:0 1px #171421}
.skill-desc {color:#c7bdd1;font-size:8px}
.gold-text {color:#ffd15c}
.small-note {font-size:8px;color:#c7bdd1;line-height:2.2}

/* MOBILE */
@media(max-width:700px) {
    #game {min-height:1100px}
    #topbar {padding:0 8px;height:55px}
    #brand {font-size:10px}
    .topstat {font-size:7px}
    #left {top:80px;left:5px;gap:10px}
    .side-btn {width:65px;height:65px;font-size:7px}
    .side-icon {font-size:22px}
    #skillBtn {top:75px;left:44%;width:90px;height:70px;font-size:7px}
    #skillBtn:active,#skillBtn.pressed {transform:translateX(-65%) translateY(6px) scale(.98)}
    #moreBtn {top:75px;left:calc(44% + 100px);width:70px;height:70px;font-size:7px}
    #center {top:200px;width:92%;min-height:330px;gap:15px}
    .ball,.split-daughter {width:83px;height:83px;border-width:8px}
    .split-daughter:after {width:28px;height:8px;left:10px;top:9px}
    #stats {top:560px;right:8px;width:47%;gap:9px}
    .stat {font-size:7px;padding:8px;min-height:75px}
    .upgrade-btn {font-size:7px}
    #bottom {bottom:30px;width:95%;gap:10px}
    .big-btn {height:85px;font-size:13px}
    #splitInfo {font-size:12px}
    #cooldown {font-size:7px}
}
</style>
</head>
<body>
<div id="game">

<div id="topbar">
    <div id="brand">CELL TYCOON</div>
    <div class="topstat green">$<span id="money">0</span></div>
    <div class="topstat gold">REBIRTH <span id="rebirths">0</span></div>
    <div class="topstat">CELLS <span id="ballCount">1</span></div>
</div>

<div id="left">
    <button class="side-btn pixel-btn" onclick="openShop()">
        <span class="side-icon">🛒</span>SHOP
    </button>
    <button class="side-btn pixel-btn" onclick="rebirth()">
        <span class="side-icon">🔄</span>REBIRTH
    </button>
    <button class="side-btn pixel-btn" onclick="openCollection()">
        <span class="side-icon">🧬</span>COLLECTION
    </button>
</div>

<button id="skillBtn" class="pixel-btn" onclick="openSkills()">🔵<br>SKILL TREE</button>
<button id="moreBtn" class="pixel-btn" onclick="openMore()">⬆<br>MORE</button>

<div id="center"></div>

<div id="stats">
    <div class="stat">
        <div class="stat-head">BALL VALUE <span class="price">$<span id="valueCost">10</span></span></div>
        <button class="upgrade-btn pixel-btn" onclick="buyUpgrade('value')">
            $<span id="value">1</span> &gt; $<span id="nextValue">2</span> A BALL<br>CLICK TO UPGRADE
        </button>
    </div>
    <div class="stat">
        <div class="stat-head">SPLIT SPEED <span class="price">$<span id="speedCost">10</span></span></div>
        <button class="upgrade-btn pixel-btn" onclick="buyUpgrade('speed')">
            <span id="speed">5.0</span> &gt; <span id="nextSpeed">4.9</span> SEC<br>CLICK TO UPGRADE
        </button>
    </div>
    <div class="stat">
        <div class="stat-head">CAPACITY <span class="price">$<span id="capacityCost">10</span></span></div>
        <button class="upgrade-btn pixel-btn" onclick="buyUpgrade('capacity')">
            <span id="capacity">16</span> &gt; <span id="nextCapacity">18</span> BALLS<br>CLICK TO UPGRADE
        </button>
    </div>
</div>

<div id="bottom">
    <span id="splitInfo">X2</span>
    <span id="cooldown"></span>
    <button id="splitBtn" class="big-btn pixel-btn" onclick="splitBalls()">SPLIT</button>
    <button id="sellBtn" class="big-btn pixel-btn" onclick="sellBalls()">SELL</button>
</div>

<div id="message"></div>
</div>

<div id="modal">
    <div id="modalBox">
        <div id="modalTitle">SHOP</div>
        <div id="modalContent"></div>
        <button class="close-btn pixel-btn" onclick="closeModal()">CLOSE</button>
    </div>
</div>

<script>
"use strict";

const DEFAULT = {
    version:3,
    money:0,
    balls:1,
    ballValue:1,
    splitSpeed:5,
    capacity:16,
    valueCost:10,
    speedCost:10,
    capacityCost:10,
    rebirths:0,
    skin:"red",
    owned:["red"],
    skillPoints:0,
    skills:{money:0,speed:0,cells:0},
    totalSold:0,
    totalSplits:0,
    totalEarned:0
};

let state={...DEFAULT,skills:{...DEFAULT.skills}};
let nextSplit=0;
let nextSell=0;
let animating=false;
let messageTimer=null;

const skins={
    red:{name:"Classic Red",color:"#ed1010",dark:"#850808",light:"#ff7777",price:0},
    blue:{name:"Ocean Blue",color:"#1687ef",dark:"#07509d",light:"#82d4ff",price:150},
    green:{name:"Toxic Green",color:"#44dc4e",dark:"#168321",light:"#a2ff91",price:300},
    purple:{name:"Royal Purple",color:"#9c54e9",dark:"#53238c",light:"#d5a2ff",price:600},
    gold:{name:"Golden Cell",color:"#ffc52e",dark:"#9d6500",light:"#fff19a",price:1200},
    pink:{name:"Galaxy Pink",color:"#ff66c8",dark:"#a32679",light:"#ffc2e8",price:2500}
};

function loadGame(){
    try{
        const saved=JSON.parse(localStorage.getItem("cell_tycoon_save"));
        if(saved && saved.version===3){
            state={...DEFAULT,...saved};
            state.skills={...DEFAULT.skills,...(saved.skills||{})};
            if(!Array.isArray(state.owned))state.owned=["red"];
            if(!state.owned.includes("red"))state.owned.push("red");
            if(!skins[state.skin])state.skin="red";
        }
    }catch(e){console.log("Starting a new game.");}
}

function saveGame(){
    try{
        localStorage.setItem("cell_tycoon_save",JSON.stringify(state));
    }catch(e){console.log("Save unavailable.");}
}

function notify(text){
    const el=document.getElementById("message");
    el.innerText=text;
    el.style.display="block";
    clearTimeout(messageTimer);
    messageTimer=setTimeout(()=>el.style.display="none",2300);
}

/* Shared click animation for every button */
document.addEventListener("pointerdown",e=>{
    const btn=e.target.closest("button");
    if(btn && !btn.disabled)btn.classList.add("pressed");
});
function releaseButtons(){
    document.querySelectorAll("button.pressed").forEach(b=>b.classList.remove("pressed"));
}
document.addEventListener("pointerup",releaseButtons);
document.addEventListener("pointercancel",releaseButtons);
document.addEventListener("pointerleave",releaseButtons);

/* Rendering */
function render(){
    document.getElementById("money").innerText=Math.floor(state.money).toLocaleString();
    document.getElementById("rebirths").innerText=state.rebirths;
    document.getElementById("ballCount").innerText=state.balls;

    document.getElementById("value").innerText=state.ballValue;
    document.getElementById("nextValue").innerText=state.ballValue+1;
    document.getElementById("valueCost").innerText=state.valueCost;

    document.getElementById("speed").innerText=state.splitSpeed.toFixed(1);
    document.getElementById("nextSpeed").innerText=Math.max(.5,state.splitSpeed-.1).toFixed(1);
    document.getElementById("speedCost").innerText=state.speedCost;

    document.getElementById("capacity").innerText=state.capacity;
    document.getElementById("nextCapacity").innerText=state.capacity+2;
    document.getElementById("capacityCost").innerText=state.capacityCost;

    const center=document.getElementById("center");
    center.innerHTML="";
    const skin=skins[state.skin]||skins.red;
    const count=Math.min(state.balls,16);

    for(let i=0;i<count;i++){
        const ball=document.createElement("div");
        ball.className="ball";
        ball.style.setProperty("--ball",skin.color);
        ball.style.setProperty("--dark",skin.dark);
        ball.style.setProperty("--light",skin.light);
        ball.style.animationDelay=(i*.08)+"s";
        center.appendChild(ball);
    }

    if(state.balls>16){
        const extra=document.createElement("div");
        extra.style.fontSize="13px";
        extra.innerText="+"+(state.balls-16)+" MORE CELLS";
        center.appendChild(extra);
    }
    saveGame();
}

function coinEffect(amount){
    const el=document.createElement("div");
    el.className="coin-float";
    el.innerText="+$"+amount.toLocaleString();
    el.style.left="50%";
    el.style.top="55%";
    document.getElementById("game").appendChild(el);
    setTimeout(()=>el.remove(),1100);
}

/* Animation duration always matches split cooldown */
function animationDuration(){
    return Math.max(.5,state.splitSpeed);
}

/* Actual cell splitting animation:
   Each parent cell disappears while two daughter cells move apart. */
function splitBalls(){
    if(animating)return;
    const now=Date.now();

    if(now<nextSplit){
        notify("WAIT FOR THE SPLIT COOLDOWN!");
        return;
    }
    if(state.balls>=state.capacity){
        notify("MAXIMUM CAPACITY! UPGRADE CAPACITY.");
        return;
    }

    const oldCount=state.balls;
    const amount=Math.min(oldCount,state.capacity-oldCount);
    const center=document.getElementById("center");
    const parents=[...center.querySelectorAll(".ball")];
    const skin=skins[state.skin]||skins.red;
    const duration=animationDuration();

    animating=true;
    nextSplit=now+duration*1000;
    nextSell=now+duration*1000;

    const overlay=document.createElement("div");
    overlay.className="split-overlay";
    center.appendChild(overlay);

    const centerRect=center.getBoundingClientRect();

    parents.forEach(parent=>{
        const rect=parent.getBoundingClientRect();
        const x=rect.left-centerRect.left;
        const y=rect.top-centerRect.top;

        parent.classList.add("split-parent");

        ["left","right"].forEach(side=>{
            const daughter=document.createElement("div");
            daughter.className="split-daughter "+side;
            daughter.style.left=x+"px";
            daughter.style.top=y+"px";
            daughter.style.setProperty("--ball",skin.color);
            daughter.style.setProperty("--dark",skin.dark);
            daughter.style.setProperty("--light",skin.light);
            daughter.style.setProperty("--duration",duration+"s");
            overlay.appendChild(daughter);
        });
    });

    notify("CELL DIVISION IN PROGRESS!");

    setTimeout(()=>{
        state.balls+=amount;
        state.totalSplits++;
        animating=false;
        render();
        notify("MITOSIS COMPLETE! +"+amount+" CELLS!");
    },duration*1000);
}

/* Selling animation lasts for the same duration */
function sellBalls(){
    if(animating)return;
    const now=Date.now();

    if(now<nextSell){
        notify("SELLING IS ON COOLDOWN!");
        return;
    }
    if(state.balls<=0){
        notify("NO CELLS TO SELL!");
        return;
    }

    const duration=animationDuration();
    const earned=Math.floor(
        state.balls*state.ballValue*
        (1+state.rebirths*.1)*
        (1+state.skills.money*.05)
    );

    animating=true;
    nextSell=now+duration*1000;
    nextSplit=now+duration*1000;

    const balls=[...document.querySelectorAll("#center .ball")];
    balls.forEach((ball,i)=>{
        ball.classList.add("selling-ball");
        ball.style.setProperty("--duration",duration+"s");
        ball.style.animationDelay=(i*.035)+"s";
    });

    notify("SELLING YOUR CELLS...");

    setTimeout(()=>{
        state.money+=earned;
        state.totalSold+=state.balls;
        state.totalEarned+=earned;
        state.balls=1;
        animating=false;
        render();
        coinEffect(earned);
        notify("SOLD! +$"+earned.toLocaleString());
    },duration*1000);
}

/* Upgrade buttons */
function buyUpgrade(type){
    if(animating)return;
    let cost=0;
    let success=false;

    if(type==="value"){
        cost=state.valueCost;
        if(state.money>=cost){
            state.money-=cost;
            state.ballValue++;
            state.valueCost=Math.floor(cost*1.65);
            success=true;
        }
    }

    if(type==="speed"){
        cost=state.speedCost;
        if(state.money>=cost && state.splitSpeed>.5){
            state.money-=cost;
            state.splitSpeed=Math.max(.5,Math.round((state.splitSpeed-.1)*10)/10);
            state.speedCost=Math.floor(cost*1.7);
            success=true;
        }else if(state.splitSpeed<=.5){
            notify("SPLIT SPEED IS AT MAXIMUM!");
            return;
        }
    }

    if(type==="capacity"){
        cost=state.capacityCost;
        if(state.money>=cost){
            state.money-=cost;
            state.capacity+=2;
            state.capacityCost=Math.floor(cost*1.6);
            success=true;
        }
    }

    if(success){
        render();
        notify("UPGRADE PURCHASED!");
    }else{
        notify("NOT ENOUGH MONEY!");
    }
}

/* Modal system */
function openModal(title,html){
    document.getElementById("modalTitle").innerText=title;
    document.getElementById("modalContent").innerHTML=html;
    document.getElementById("modal").style.display="flex";
}
function closeModal(){
    document.getElementById("modal").style.display="none";
}

/* Shop */
function openShop(){
    let html="";
    Object.keys(skins).forEach(id=>{
        const s=skins[id];
        const owned=state.owned.includes(id);
        const equipped=state.skin===id;

        html+=`
        <div class="modal-item">
            <span>
                <span style="color:${s.color};font-size:18px">●</span><br>
                ${s.name}<br>${s.price===0?"FREE":"$"+s.price}
            </span>
            <button class="pixel-btn" onclick="buySkin('${id}')">
                ${equipped?"EQUIPPED":owned?"EQUIP":"BUY"}
            </button>
        </div>`;
    });
    openModal("CELL SKIN SHOP",html);
}

function buySkin(id){
    const s=skins[id];
    if(!s)return;

    if(state.owned.includes(id)){
        state.skin=id;
        render();
        openShop();
        notify("CELL EQUIPPED!");
        return;
    }
    if(state.money<s.price){
        notify("NOT ENOUGH MONEY!");
        return;
    }

    state.money-=s.price;
    state.owned.push(id);
    state.skin=id;
    render();
    openShop();
    notify("NEW CELL UNLOCKED!");
}

/* Skill tree */
function openSkills(){
    const skills=[
        {id:"money",name:"MONEY MASTERY",icon:"💰",desc:"+5% selling income per level",cost:1},
        {id:"speed",name:"QUICK DIVISION",icon:"⚡",desc:"Improves split speed permanently",cost:2},
        {id:"cells",name:"CELL EXPANSION",icon:"🧬",desc:"+2 starting cells and capacity",cost:3}
    ];

    let html=`
    <div class="modal-item">
        <span>AVAILABLE SKILL POINTS</span>
        <span class="gold-text">${state.skillPoints}</span>
    </div>`;

    skills.forEach(s=>{
        html+=`
        <div class="modal-item">
            <span>
                ${s.icon} ${s.name}<br>
                <span class="skill-desc">${s.desc}</span><br>
                LEVEL ${state.skills[s.id]} | COST ${s.cost} POINTS
            </span>
            <button class="pixel-btn" onclick="buySkill('${s.id}')">UNLOCK</button>
        </div>`;
    });

    openModal("🌳 SKILL TREE",html);
}

function buySkill(id){
    const costs={money:1,speed:2,cells:3};
    const cost=costs[id];

    if(!cost){
        notify("INVALID SKILL!");
        return;
    }
    if(state.skillPoints<cost){
        notify("NOT ENOUGH SKILL POINTS!");
        return;
    }

    state.skillPoints-=cost;
    state.skills[id]++;

    if(id==="speed"){
        state.splitSpeed=Math.max(.5,Math.round((state.splitSpeed-.2)*10)/10);
    }
    if(id==="cells"){
        state.capacity+=2;
    }

    render();
    openSkills();
    notify("SKILL UNLOCKED!");
}

/* Rebirth */
function rebirth(){
    if(animating)return;
    const requirement=10000*(state.rebirths+1);

    if(state.money<requirement){
        notify("YOU NEED $"+requirement.toLocaleString()+" TO REBIRTH!");
        return;
    }

    if(!confirm("REBIRTH NOW? Your money and normal upgrades reset. You gain 1 Skill Point and a permanent bonus."))return;

    state.money=0;
    state.balls=1+state.skills.cells*2;
    state.ballValue=1;
    state.splitSpeed=5;
    state.capacity=16+state.skills.cells*2;
    state.valueCost=10;
    state.speedCost=10;
    state.capacityCost=10;
    state.rebirths++;
    state.skillPoints++;
    nextSplit=0;
    nextSell=0;

    render();
    notify("REBIRTH COMPLETE! +1 SKILL POINT!");
}

/* Collection */
function openCollection(){
    const html=`
    <div class="modal-item"><span>TOTAL CELLS SOLD</span><span>${state.totalSold}</span></div>
    <div class="modal-item"><span>TOTAL SPLITS</span><span>${state.totalSplits}</span></div>
    <div class="modal-item"><span>TOTAL MONEY EARNED</span><span>$${state.totalEarned.toLocaleString()}</span></div>
    <div class="modal-item"><span>SKINS OWNED</span><span>${state.owned.length}/${Object.keys(skins).length}</span></div>
    <div class="modal-item"><span>REBIRTHS</span><span>${state.rebirths}</span></div>
    <div class="modal-item"><span>SKILL POINTS</span><span>${state.skillPoints}</span></div>`;
    openModal("YOUR COLLECTION",html);
}

/* More */
function openMore(){
    const html=`
    <div class="modal-item"><span>GAME GUIDE<br><span class="skill-desc">Split cells, sell them, and buy upgrades.</span></span></div>
    <div class="modal-item"><span>SELLING BONUS</span><span>+${state.rebirths*10+state.skills.money*5}%</span></div>
    <div class="modal-item"><span>YOUR CELLS</span><span>${state.balls}</span></div>
    <div class="modal-item"><span>CAPACITY</span><span>${state.capacity}</span></div>
    <div class="modal-item"><span>GAME VERSION</span><span>3.0</span></div>
    <div class="modal-item"><span>RESET SAVE DATA</span><button class="pixel-btn" onclick="resetGame()">RESET</button></div>`;
    openModal("MORE OPTIONS",html);
}

function resetGame(){
    if(!confirm("Delete ALL your progress?"))return;
    state={...DEFAULT,skills:{...DEFAULT.skills},owned:["red"]};
    nextSplit=0;
    nextSell=0;
    animating=false;
    render();
    closeModal();
    notify("NEW GAME STARTED!");
}

/* Cooldown display */
function updateCooldown(){
    const now=Date.now();
    const remaining=Math.max(0,nextSplit-now);
    const sellRemaining=Math.max(0,nextSell-now);

    document.getElementById("cooldown").innerText=
        animating ? "DIVIDING..." :
        remaining>0 ? (remaining/1000).toFixed(1)+" SEC" : "";

    document.getElementById("splitBtn").style.opacity=
        (animating||remaining>0) ? ".65" : "1";
    document.getElementById("sellBtn").style.opacity=
        (animating||sellRemaining>0) ? ".65" : "1";
}

loadGame();
render();
setInterval(updateCooldown,100);
</script>
</body>
</html>
"""

components.html(GAME, height=1000, scrolling=True)

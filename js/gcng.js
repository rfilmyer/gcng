"use strict";

function pickRandomElement(arr){
	const length = arr.length
	const randomIndex = Math.floor(Math.random() * length)
	return arr[randomIndex]
}

function createName(nameList){
	const nameParts = nameList["names"].map((list) => pickRandomElement(nameList[list]))
	return nameParts.join(" ")
}

function replaceCommunityName(nameList) {
	const community = document.querySelector("#community")
	community.innerText = createName(nameList)
	document.querySelector("#tagline").innerText = pickRandomElement(nameList["taglines"])
}

const oReq = new XMLHttpRequest();
oReq.responseType = "json"
oReq.addEventListener("load", () => replaceCommunityName(oReq.response));
oReq.open("GET", "/communities.json");
oReq.send();
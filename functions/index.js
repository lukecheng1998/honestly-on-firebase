const functions = require("firebase-functions");
const admin = require("firebase-admin");
const app = require("express")();
const { db } = require("./util/admin");

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.api = functions.https.onRequest(app);
const { search, getSearch } = require("./handlers/search");
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });

//Method to get results from the python script and decompose it

//Search routes
app.post("/searches", search);
app.get("/searches", getSearch);


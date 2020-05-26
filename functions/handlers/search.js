const { admin, db } = require("../util/admin");
const config = require("../util/config");
const firebase = require("firebase");
firebase.initializeApp(config);

//Writes a search into the database
exports.search = (req, res) => {
  //create a new searched algorithm that will use the textfield to send out a request to the python script
  // if(req.body.trim() === ''){
  //     return res.status(400).json({body: 'Textfield can not be empty' });
  // }
  const searched = {
    textfield: req.body.textfield,
    results: req.body.results,
  };
  db.collection("searches")
    //before calling .add we will call the python script here and pass in the variable here
    .add(searched)
    .then((doc) => {
      const resSearched = searched;
      res.json(resSearched);
    })
    .catch((err) => {
      res.status(500).json({ error: "Something went wrong try again!" });
      console.log(err);
    });
};
exports.getSearch = (req, res) => {
    let searchData = {};
    db.doc(`/searches/${req.params.textfield}`).get()
    .then( doc => {
        if(doc.exists){
            searchData.searches
        }
    })
}
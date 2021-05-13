//const axios = require("axios");
//import VueSocketio from 'vue-socket.io';


const RollDice = {
  el: '#RollDice',
  data() {
    return {
      dRoll: ''
    };
  },
  methods: {
    rollDice (mod){
      this.dRoll = Math.floor(Math.random() * Math.floor(20))+1+mod; //return a roll of a d20
    },
  },
};

Vue.createApp(RollDice).mount('#RollDice');

const ListRendering = {
  data() {
    return {
      characters: [],
    };
  },
  mounted() {
    //get request
    //get results
    axios
      .get("/characters/")
      .then(function (response) {
        // handle success
        myapp.characters = response.data.characters;
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      });
    setInterval(() => {
      axios
        .get("/characters/")
        .then(function (response) {
          // handle success
          myapp.characters = response.data.characters;
          console.log(response);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
      //get request
      //get results
    }, 100000);
  },
};

const myapp = Vue.createApp(ListRendering).mount("#list-rendering");

const rolls = [
  {
    options: {
    Acrobatics:"DEX",
    AnimalHandling:"WIS",
    Arcana:"INT",
    Athletics: "STR",
    Deception: "CHA",
    History:"INT",
    Insight:"WIS",
    Intimidation:"CHA",
    Investigation: "INT",
    Medicine:"WIS",
    Nature:"INT",
    Perception: "WIS",
    Performance: "CHA",
    Persuasion: "CHA",
    Religion: "INT",
    SleightOfHand: "DEX",
    Stealth: "DEX",
    Survival: "WIS",
  },
  selectedValue: '',
  }
]

const FunctionRendering = {
  data() {
    return {
      character:[],
      dRoll: '',
      rolls,
    };
  },
  mounted() {
    //get request
    //get results
    axios
      .get("/functionz/")
      .then(function (response) {
        // handle success
        charfunc.character = response.data;
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      });
    setInterval(() => {
      axios
        .get("/functionz/")
        .then(function (response) {
          // handle success
          charfunc.character = response.data;
          console.log(response);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
      //get request
      //get results
    }, 100000);
  },
  methods: {
    getMod(attr){
      if(attr == "DEX"){
        return Math.floor((this.character["dexterity"]-10)/2)
      }
      else if(attr == "INT"){
        return Math.floor((this.character["intelligence"]-10)/2)
      }
      else if(attr == "CHA"){
        return Math.floor((this.character["charisma"]-10)/2)
      }
      else if(attr == "WIS"){
        return Math.floor((this.character["wisdom"]-10)/2)
      }
      else if(attr == "STR"){
        return Math.floor((this.character["strength"]-10)/2)
      }
      else{
        return 0
      }
    },
    rollDice (){
      this.dRoll = Math.floor(Math.random() * Math.floor(20))+1+this.getMod(rolls.selectedValue); //return a roll of a d20
    },
  },
};

const charfunc = Vue.createApp(FunctionRendering).mount("#function-rendering");

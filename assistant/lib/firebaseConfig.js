import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyDE2c5q_6ILw3u04Gjs2Wskmaqw2vSPePQ",
  authDomain: "my-first-project-a6406.firebaseapp.com",
  projectId: "my-first-project-a6406",
  storageBucket: "my-first-project-a6406.appspot.com",
  messagingSenderId: "354299790602",
  appId: "1:354299790602:web:ab1bb9cf8442ffa6eca6f3",
  measurementId: "G-165FF2C506"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firestore
export const db = getFirestore(app);
console.log(db)
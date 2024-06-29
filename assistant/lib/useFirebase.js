"use client";

import { useState, useEffect } from "react";
import { db } from "./firebaseConfig";
import { collection, getDocs, addDoc, deleteDoc, doc, updateDoc } from 'firebase/firestore'

const NOTES_COLLECTION = "notes";
const TODOS_COLLECTION = "todos";

export default function useFirebase() {
  const [notes, setNotes] = useState([]);
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchNotes = async () => {
    try {
      const notesCollection = collection(db, NOTES_COLLECTION);
      const snapshot = await getDocs(notesCollection);
      const notesData = snapshot.docs.map((doc) => ({
        id: doc.id,
        ...doc.data(),
      }));
      setNotes(notesData);
    } catch (error) {
      console.error("Error fetching notes:", error);
    }
  };

  const fetchTodos = async () => {
    try {
      const todosCollection = collection(db, TODOS_COLLECTION);
      const snapshot = await getDocs(todosCollection);
      const todosData = snapshot.docs.map((doc) => ({
        id: doc.id,
        ...doc.data(),
      }));
      setTodos(todosData);
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      await fetchNotes();
      await fetchTodos();
      setLoading(false);
    };

    fetchData();
  }, []);

  const addNote = async (category, text) => {
    try {
      const date = new Date();
      const notesCollection = collection(db, NOTES_COLLECTION);
      await addDoc(notesCollection, { category, text, date });
      fetchNotes();
    } catch (error) {
      console.error("Error adding note:", error);
    }
  };

  const addTodo = async (item, category, done = false) => {
    try {
      const date = new Date();
      const todosCollection = collection(db, TODOS_COLLECTION);
      await addDoc(todosCollection, { item, category, done, date });
      fetchTodos();
    } catch (error) {
      console.error("Error adding todo:", error);
    }
  };

  const updateNote = async (id, updatedNote) => {
    try {
      const noteDoc = doc(db, NOTES_COLLECTION, id);
      await updateDoc(noteDoc, updatedNote);
      fetchNotes();
    } catch (error) {
      console.error("Error updating note:", error);
    }
  };

  const updateTodo = async (id, updatedTodo) => {
    try {
      const todoDoc = doc(db, TODOS_COLLECTION, id);
      await updateDoc(todoDoc, updatedTodo);
      fetchTodos();
    } catch (error) {
      console.error("Error updating todo:", error);
    }
  };

  const deleteNote = async (id) => {
    try {
      const noteDoc = doc(db, NOTES_COLLECTION, id);
      await deleteDoc(noteDoc);
      fetchNotes();
    } catch (error) {
      console.error("Error deleting note:", error);
    }
  };

  const deleteTodo = async (id) => {
    try {
      const todoDoc = doc(db, TODOS_COLLECTION, id);
      await deleteDoc(todoDoc);
      fetchTodos();
    } catch (error) {
      console.error("Error deleting todo:", error);
    }
  };

  return {
    notes,
    todos,
    loading,
    addNote,
    addTodo,
    updateNote,
    updateTodo,
    deleteNote,
    deleteTodo,
  };
}

"use client";
import React from "react";
import { FaSpinner } from 'react-icons/fa';
import useFirebase from "@/lib/useFirebase";

const NotesCard = () => {
  const { notes, loading } = useFirebase();

  if (loading) {
    return <div className="flex justify-center items-center h-32"><FaSpinner className="animate-spin text-gray-700 text-2xl" /></div>;
  }

  return (
    <div className="notes-container p-6 bg-white shadow-lg rounded-lg max-w-sm mx-auto md:max-w-md border border-gray-300">
      <h2 className="text-2xl font-bold mb-4 text-black">Notes</h2>
      {notes.length > 0 ? (
        <div className="notes-list max-h-96 overflow-y-auto md:max-h-[24rem]">
          {notes.map((note) => (
            <div key={note.id} className="note-card mb-4 p-4 border rounded-lg shadow-sm bg-gray-100">
              <h3 className="text-xl font-semibold text-black">{note.category}</h3>
              <p className="text-black">{note.text}</p>
            </div>
          ))}
        </div>
      ) : (
        <div className="text-gray-700">No notes available.</div>
      )}
    </div>
  );
};

export default NotesCard;

import Head from "next/head";

export default function Layout({ children }) {
  return (

      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Hi, Fai!</h1>
        {children}
      </div>
  );
}
import Head from "next/head";

export default function Layout({ children }) {
  return (
    <html>
      <Head>
        <title>Productivity Dashboard</title>
      </Head>
      <body>
      <main className="container mx-auto px-4 py-8">
        {children}
      </main>
      </body>
     </html>
  );
}

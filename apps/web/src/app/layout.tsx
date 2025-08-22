import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { Providers } from '@/components/providers';
import { Toaster } from 'react-hot-toast';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Recruitment Flow AI - Intelligent Hiring Orchestration',
  description: 'Source. Screen. Schedule. Decide—fairly and fast. Intelligent hiring orchestration platform that automates role intake, job description creation, sourcing, screening, interview scheduling, evaluation, and offer workflows.',
  keywords: 'recruitment, AI, hiring, talent acquisition, interview scheduling, candidate screening',
  authors: [{ name: 'Recruitment Flow AI Team' }],
  viewport: 'width=device-width, initial-scale=1',
  robots: 'index, follow',
  openGraph: {
    title: 'Recruitment Flow AI - Intelligent Hiring Orchestration',
    description: 'Source. Screen. Schedule. Decide—fairly and fast.',
    type: 'website',
    locale: 'en_US',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Recruitment Flow AI - Intelligent Hiring Orchestration',
    description: 'Source. Screen. Schedule. Decide—fairly and fast.',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="h-full">
      <body className={`${inter.className} h-full bg-gray-50 dark:bg-gray-900`}>
        <Providers>
          {children}
          <Toaster
            position="top-right"
            toastOptions={{
              duration: 4000,
              style: {
                background: '#363636',
                color: '#fff',
              },
              success: {
                duration: 3000,
                iconTheme: {
                  primary: '#22c55e',
                  secondary: '#fff',
                },
              },
              error: {
                duration: 5000,
                iconTheme: {
                  primary: '#ef4444',
                  secondary: '#fff',
                },
              },
            }}
          />
        </Providers>
      </body>
    </html>
  );
}

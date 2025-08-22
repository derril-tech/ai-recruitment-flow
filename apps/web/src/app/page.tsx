import { Metadata } from 'next';
import { DashboardLayout } from '@/components/layouts/dashboard-layout';
import { PipelineBoard } from '@/components/dashboard/pipeline-board';
import { QuickStats } from '@/components/dashboard/quick-stats';
import { RecentActivity } from '@/components/dashboard/recent-activity';

export const metadata: Metadata = {
  title: 'Dashboard - Recruitment Flow AI',
  description: 'Overview of your recruitment pipeline and key metrics',
};

export default function DashboardPage() {
  return (
    <DashboardLayout>
      <div className="space-y-6">
        {/* Page Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
              Dashboard
            </h1>
            <p className="text-gray-600 dark:text-gray-400">
              Overview of your recruitment pipeline and key metrics
            </p>
          </div>
          <div className="flex space-x-3">
            <button className="btn btn-outline">
              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
              </svg>
              New Role
            </button>
            <button className="btn btn-primary">
              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
              </svg>
              Import Candidates
            </button>
          </div>
        </div>

        {/* Quick Stats */}
        <QuickStats />

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Pipeline Board */}
          <div className="lg:col-span-2">
            <PipelineBoard />
          </div>

          {/* Recent Activity */}
          <div className="lg:col-span-1">
            <RecentActivity />
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
}

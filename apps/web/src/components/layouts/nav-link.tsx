'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { clsx } from 'clsx';
import {
  HomeIcon,
  BriefcaseIcon,
  UsersIcon,
  CalendarIcon,
  DocumentTextIcon,
  ChartBarIcon,
  ShieldCheckIcon,
  CogIcon,
} from '@heroicons/react/24/outline';

interface NavItem {
  name: string;
  href: string;
  icon: string;
}

interface NavLinkProps {
  item: NavItem;
}

const iconMap = {
  HomeIcon,
  BriefcaseIcon,
  UsersIcon,
  CalendarIcon,
  DocumentTextIcon,
  ChartBarIcon,
  ShieldCheckIcon,
  CogIcon,
};

export function NavLink({ item }: NavLinkProps) {
  const pathname = usePathname();
  const Icon = iconMap[item.icon as keyof typeof iconMap];
  
  const isActive = pathname === item.href || pathname.startsWith(item.href + '/');

  return (
    <li>
      <Link
        href={item.href}
        className={clsx(
          isActive
            ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-700 dark:text-primary-300'
            : 'text-gray-700 dark:text-gray-300 hover:text-primary-700 dark:hover:text-primary-300 hover:bg-primary-50 dark:hover:bg-primary-900/20',
          'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-medium transition-colors'
        )}
      >
        <Icon
          className={clsx(
            isActive ? 'text-primary-700 dark:text-primary-300' : 'text-gray-400 group-hover:text-primary-700 dark:group-hover:text-primary-300',
            'h-6 w-6 shrink-0 transition-colors'
          )}
          aria-hidden="true"
        />
        {item.name}
      </Link>
    </li>
  );
}

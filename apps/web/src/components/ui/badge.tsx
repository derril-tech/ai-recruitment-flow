import { forwardRef, HTMLAttributes } from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils';

const badgeVariants = cva(
  'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2',
  {
    variants: {
      variant: {
        default:
          'bg-primary-100 text-primary-800 dark:bg-primary-900 dark:text-primary-200',
        secondary:
          'bg-secondary-100 text-secondary-800 dark:bg-secondary-900 dark:text-secondary-200',
        destructive:
          'bg-error-100 text-error-800 dark:bg-error-900 dark:text-error-200',
        outline:
          'text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700',
        success:
          'bg-success-100 text-success-800 dark:bg-success-900 dark:text-success-200',
        warning:
          'bg-warning-100 text-warning-800 dark:bg-warning-900 dark:text-warning-200',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
);

export interface BadgeProps
  extends HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

const Badge = forwardRef<HTMLDivElement, BadgeProps>(
  ({ className, variant, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(badgeVariants({ variant }), className)}
      {...props}
    />
  )
);
Badge.displayName = 'Badge';

export { Badge, badgeVariants };

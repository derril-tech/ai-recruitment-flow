# UI Package Instructions

## Purpose
This package contains shared UI components used across the Recruitment Flow AI application.

## Development Guidelines
- All components should be built with TypeScript and React
- Use Tailwind CSS for styling
- Implement proper accessibility (ARIA labels, keyboard navigation)
- Support both light and dark themes
- Include proper TypeScript interfaces for all props
- Add JSDoc comments for complex components

## Component Structure
```
src/
  components/
    Button/
      Button.tsx
      Button.test.tsx
      index.ts
    Card/
      Card.tsx
      Card.test.tsx
      index.ts
    Form/
      FormField.tsx
      FormField.test.tsx
      index.ts
  utils/
    cn.ts
    variants.ts
  index.ts
```

## TODO: Implement Core Components
- [ ] Button (primary, secondary, outline, ghost variants)
- [ ] Card (header, content, footer sections)
- [ ] Form components (input, select, textarea, checkbox, radio)
- [ ] Badge (status indicators)
- [ ] Modal/Dialog
- [ ] Dropdown/Menu
- [ ] Table
- [ ] Pagination
- [ ] Loading states
- [ ] Toast notifications

## Testing Requirements
- Unit tests for all components
- Accessibility testing
- Visual regression testing
- Storybook integration for component documentation

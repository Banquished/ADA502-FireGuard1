import { render, screen } from '@testing-library/react';
import App from './App';

// Mock child components
jest.mock('./Components/Header', () => () => <div>Header component</div>);
jest.mock('./Components/Router', () => () => <div>Router component</div>);

// Test that App renders Header and Router components properly
test('renders Header and Router components', () => {
  render(<App />);
  expect(screen.getByText('Header component')).toBeInTheDocument();
  expect(screen.getByText('Router component')).toBeInTheDocument();
});

// Indiviudal component tests
// Header

// Router

// GoogleMaps

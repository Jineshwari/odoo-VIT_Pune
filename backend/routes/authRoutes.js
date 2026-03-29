import express from 'express';
import { register, login, createEmployee, adminDashboard, adminDashboardApprovalRules } from '../controllers/authController.js';
import { protect, authorize } from '../middleware/authMiddleware.js';
import { getExpenses, getManagerExpenses, createExpense } from '../controllers/authController.js';

const router = express.Router();

// Auth routes
router.post('/register', register);
router.post('/login', login);


// Admin routes
router.post('/employees', protect, authorize('admin'), createEmployee);
router.post('/admin-dashboard', protect, authorize('admin'), adminDashboard);
router.post('/admin-dashboard/approval-rules', protect, authorize('admin'), adminDashboardApprovalRules);
router.get('/employees', protect, authorize('admin'), adminDashboard);
router.post('/expenses', protect, authorize('employee'), createExpense);
// Employee → view own expenses
router.get('/expenses', protect, authorize('employee'), getExpenses);

// Manager → view team expenses
router.get('/manager-expenses', protect, authorize('manager'), getManagerExpenses);

// Create expense
router.post('/expenses', protect, authorize('employee'), createExpense);
// or create a new controller method getEmployees


export default router;

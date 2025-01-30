/**
 * Authentication Slice
 *
 * This slice manages the authentication state of the application using Redux Toolkit.
 * It handles user authentication data, tokens, and authentication status.
 *
 * Features:
 * - Manages user data (role, email, name)
 * - Handles authentication tokens
 * - Tracks authentication status
 * - Provides actions for login, signup and logout
 * - Integrates with RTK Query endpoints
 *
 * State Structure:
 * - user: Object containing user role, email and name
 * - token: Authentication access token
 * - isAuthenticated: Boolean flag indicating auth status
 */

import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { apiService, AuthResponse } from '../apiServices/apiServicesLMS'

// Type definition for authentication state
interface AuthState {
  user: { role: string; email: string; name: string } | null
  token: string | null
  isAuthenticated: boolean
}

// Initial state with no user authenticated
const initialState: AuthState = {
  user: null,
  token: null,
  isAuthenticated: false,
}

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    // Action to clear auth state on logout
    logoutState: (state) => {
      state.user = null
      state.token = null
      state.isAuthenticated = false
    },
    // Action to set user data on manual login
    setUser: (state, action: PayloadAction<AuthResponse & { access_token: string }>) => {
      const { role, email, full_name, access_token } = action.payload
      state.user = { role, email, name: full_name }
      state.token = access_token
      state.isAuthenticated = true
    },
  },
  // Handle automated state updates from API endpoints
  extraReducers: (builder) => {
    builder
      // Update state on successful login
      .addMatcher(
        apiService.endpoints.login.matchFulfilled,
        (state, { payload }: { payload: AuthResponse & { access_token: string } }) => {
          state.user = {
            role: payload.role,
            email: payload.email,
            name: payload.full_name,
          }
          state.token = payload.access_token
          state.isAuthenticated = true
        }
      )
      // Update state on successful signup
      .addMatcher(
        apiService.endpoints.signup.matchFulfilled,
        (state, { payload }: { payload: AuthResponse & { access_token: string } }) => {
          state.user = {
            role: payload.role,
            email: payload.email,
            name: payload.full_name,
          }
          state.token = payload.access_token
          state.isAuthenticated = true
        }
      )
      // Clear state on successful logout
      .addMatcher(apiService.endpoints.logout.matchFulfilled, (state) => {
        state.user = null
        state.token = null
        state.isAuthenticated = false
      })
  },
})

export const { setUser, logoutState } = authSlice.actions
export default authSlice.reducer

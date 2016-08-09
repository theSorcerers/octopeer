Rails.application.routes.draw do
  namespace :api do
    resources :change_tab_events, only: [:index, :show, :create]
    resources :element_types, only: [:index, :show, :create]
    resources :event_types, only: [:index, :show, :create]
    resources :file_positions, only: [:index, :show, :create]
    resources :keystroke_events, only: [:index, :show, :create]
    resources :keystroke_types, only: [:index, :show, :create]
    resources :mouse_click_events, only: [:index, :show, :create]
    resources :mouse_position_events, only: [:index, :show, :create]
    resources :mouse_scroll_events, only: [:index, :show, :create]
    resources :pull_requests, only: [:index, :show, :create]
    resources :repositories, only: [:index, :show, :create]
    resources :semantic_events, only: [:index, :show, :create]
    resources :sessions, only: [:index, :show, :create]
    resources :users, only: [:index, :show, :create]
    resources :window_resolution_events, only: [:index, :show, :create]
  end
end

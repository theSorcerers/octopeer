Rails.application.routes.draw do
  resources :users, only: [:index, :show, :create]
  resources :repositories, only: [:index, :show, :create]
  resources :pull_requests, only: [:index, :show, :create]
end

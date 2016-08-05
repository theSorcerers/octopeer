Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :users, only: [:index, :show, :create]
      resources :repositories, only: [:index, :show, :create]
    end
  end
end

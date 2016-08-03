class Api::V1::UsersController < ApplicationController
  def index
    render json: User.all
  end

  def show
  end

  def create
  end
end

class Api::SessionsController < ApplicationController
  before_action :set_session, only: :show

  def index
    @sessions = Session.all

    render json: @sessions
  end

  def show
    render json: @session
  end

  def create
    @session = Session.new(session_params)

    if @session.save
      render json: @session, status: :created, location: @session
    else
      render json: @session.errors, status: :unprocessable_entity
    end
  end

  private

  def set_session
    @session = Session.find(params[:id])
  end

  def session_params
    params.require(:session).permit(:pull_request_id, :user_id)
  end
end

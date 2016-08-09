class Api::WindowResolutionEventsController < ApplicationController
  include TimeHelper
  before_action :set_window_resolution_event, only: :show
  before_action only: :create do
    format_time(:window_resolution_event)
  end

  def index
    @window_resolution_events = WindowResolutionEvent.all

    render json: @window_resolution_events
  end

  def show
    render json: @window_resolution_event
  end

  def create
    @window_resolution_event = WindowResolutionEvent.new(window_resolution_event_params)

    if @window_resolution_event.save
      render json: @window_resolution_event, status: :created
    else
      render json: @window_resolution_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_window_resolution_event
    @window_resolution_event = WindowResolutionEvent.find(params[:id])
  end

  def window_resolution_event_params
    params.require(:window_resolution_event).permit(:id, :width, :height, :session_id, :created_at)
  end
end

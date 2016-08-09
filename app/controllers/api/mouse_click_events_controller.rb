class Api::MouseClickEventsController < ApplicationController
  include TimeHelper
  before_action :set_mouse_click_event, only: :show
  before_action only: :create do
    format_time(:mouse_click_event)
  end

  def index
    @mouse_click_events = MouseClickEvent.all

    render json: @mouse_click_events
  end

  def show
    render json: @mouse_click_event
  end

  def create
    @mouse_click_event = MouseClickEvent.new(mouse_click_event_params)

    if @mouse_click_event.save
      render json: @mouse_click_event, status: :created
    else
      render json: @mouse_click_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_mouse_click_event
    @mouse_click_event = MouseClickEvent.find(params[:id])
  end

  def mouse_click_event_params
    params.require(:mouse_click_event).permit(:id, :session_id, :created_at)
  end
end
